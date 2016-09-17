// CIA.09.02.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <thread>
#include <future>
#include <exception>
#include <chrono>
#include <iostream>>


class interrupt_flag
{
	std::atomic<bool> flag;
	std::condition_variable* thread_cond;
	std::mutex set_clear_mutex;
public:
	interrupt_flag() : thread_cond(0) {}

	void set()
	{
		flag.store(true, std::memory_order_relaxed);
		std::lock_guard<std::mutex> lk(set_clear_mutex);
		if (thread_cond)
			thread_cond->notify_all();
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
			f();
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

int main()
{
	std::mutex MX;
	std::condition_variable CV;

	auto F1 = [&] {
		std::cout << "Start F1" << std::endl;

		try
		{
			std::unique_lock<std::mutex> UL(MX);
			while (true)
			{
				interruptible_wait(CV, UL);
			}
		}
		catch (thread_interrupted& e)
		{
			std::cout << e.what() << std::endl;
		}

		std::cout << "Endof F1" << std::endl;
	};

	interruptible_thread T1(F1);


	std::thread T2([&] {
		std::cout << "Start F2" << std::endl;
		std::this_thread::sleep_for(std::chrono::milliseconds(1000));

		T1.interrupt();

		//std::this_thread::sleep_for(std::chrono::milliseconds(10000));
		//T1.interrupt();
		std::cout << "Endof F2" << std::endl;
	});


	T1.join();
	T2.join();
	return 0;
}

