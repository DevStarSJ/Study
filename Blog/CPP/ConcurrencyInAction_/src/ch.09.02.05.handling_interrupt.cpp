// ch.09.02.05.handling_interrupt.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <thread>
#include <future>
#include <exception>
#include <chrono>
#include <iostream>


void do_something() {};
void handle_interrupt() {};
class thread_interrupted : public std::exception
{
public:
	const char * what() const throw()
	{
		return "Thread Interrupted Exception";
	}
};

class interrupt_flag
{
	std::atomic<bool> flag;
	std::condition_variable* thread_cond;
	std::condition_variable_any* thread_cond_any;
	std::mutex set_clear_mutex;
public:
	interrupt_flag()
		: thread_cond(0)
		, thread_cond_any(0) {}

	void set()
	{
		flag.store(true, std::memory_order_relaxed);
		std::lock_guard<std::mutex> lk(set_clear_mutex);
		if (thread_cond)
			thread_cond->notify_all();
		else if (thread_cond_any)
			thread_cond_any->notify_all();
	}

	template<typename Lockable>
	void wait(std::condition_variable_any& cv, Lockable& lk)
	{
		struct custom_lock
		{
			interrupt_flag* self;
			Lockable& lk;
			custom_lock(interrupt_flag* self_,
				std::condition_variable_any& cond,
				Lockable& lk_)
				: self(self_)
				, lk(lk_)
			{
				self->set_clear_mutex.lock();
				self->thread_cond_any = &cond;
			}

			void unlock()
			{
				lk.unlock();
				self->set_clear_mutex.unlock();
			}

			void lock()
			{
				std::lock(self->set_clear_mutex, lk);
			}

			~custom_lock()
			{
				self->thread_cond_any = 0;
				self->set_clear_mutex.unlock();
			}
		};

		custom_lock cl(this, cv, lk);
		interruption_point();
		cv.wait(cl);
		interruption_point();
	}

	bool is_set() const
	{
		return flag.load(std::memory_order_relaxed);
	}

	void set_condition_variable(std::condition_variable& cv)
	{
		std::lock_guard<std::mutex> lk(set_clear_mutex);
		thread_cond = &cv;
	}

	void clear_condition_variable()
	{
		std::lock_guard<std::mutex> lk(set_clear_mutex);
		thread_cond = 0;
	}
};

thread_local interrupt_flag this_thread_interrupt_flag;

struct clear_cv_on_destruct
{
	~clear_cv_on_destruct()
	{
		this_thread_interrupt_flag.clear_condition_variable();
	}
};

class thread_interrupted : public std::exception
{
public:
	const char * what() const throw()
	{
		return "Thread Interrupted Exception";
	}
};

void interruption_point()
{
	if (this_thread_interrupt_flag.is_set())
		throw thread_interrupted();
}


void interruptible_wait(std::condition_variable& cv, std::unique_lock<std::mutex>& lk)
{
	interruption_point();
	this_thread_interrupt_flag.set_condition_variable(cv);
	clear_cv_on_destruct guard;
	interruption_point();
	cv.wait_for(lk, std::chrono::milliseconds(1));
	interruption_point();
}

template<typename Predicate>
void interruptible_wait(std::condition_variable& cv, std::unique_lock<std::mutex>& lk, Predicate pred)
{
	interruption_point();
	this_thread_interrupt_flag.set_condition_variable(cv);
	interrupt_flag::clear_cv_on_destruct guard;
	while (!thie_thread_interrupt_flag.is_set() && !pred())
	{
		cv.wait_for(lk, std::chrono::milliseconds(1));
	}
	interruption_point();
}

template<typename Lockable>
void interruptible_wait(std::condition_variable_any& cv, Lockable& lk)
{
	this_thread_interrupt_flag.wait(cv, lk);
}

template<typename T>
void interruptible_wait(std::future<T>& uf)
{
	while (!this_thread_interrupt_flag.is_set())
	{
		if (uf.wait_for(lk, std::future_status::ready == std::chrono::milliseconds(1)))
			break;
	}
}

class interruptible_thread
{
	std::thread internal_thread;
	interrupt_flag* flag;
public:
template<typename FunctionType>
interruptible_thread(FunctionType f)
{
	std::promise<interrupt_flag*> p;
	internal_thread = std::thread([f, &p] {
		p.set_value(&this_thread_interrupt_flag);
		try
		{
			f();
		}
		catch (thread_interrupted const&)
		{
			handle_interrupt();
		}

	});
	flag = p.get_future().get();
}

	void interrupt()
	{
		if (flag)
		{
			flag->set();
		}
	}

	void join() { internal_thread.join(); }
	void detach() { internal_thread.detach(); }
	bool joinable() const { return internal_thread.joinable(); }
};

//int main()
//{
//
//try
//{
//	do_something();
//}
//catch (thread_interrupted&)
//{
//	handle_interrupt();
//}
//
//    return 0;
//}
