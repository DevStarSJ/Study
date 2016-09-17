// CIA.09.02.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <thread>
#include <future>
#include <exception>
#include <chrono>
#include <iostream>


class interrupt_flag
{
	std::atomic<bool> flag;
public:
	void set()
	{
		flag.store(true, std::memory_order_relaxed);
	}

	bool is_set() const
	{
		return flag.load(std::memory_order_relaxed);
	}
};


//class interrupt_flag
//{
//	std::atomic<bool> flag;
//	//std::condition_variable* thread_cond;
//	//std::mutex set_clear_mutex;
//public:
//	interrupt_flag()// : thread_cond(0)
//	{}
//
//	void set()
//	{
//		flag.store(true, std::memory_order_relaxed);
//		//std::lock_guard<std::mutex> lk(set_clear_mutex);
//		//if (thread_cond)
//		//	thread_cond->notify_all();
//	}
//
//	bool is_set() const
//	{
//		return flag.load(std::memory_order_relaxed);
//	}
//
//	void set_condition_variable(std::condition_variable& cv)
//	{
//		//std::lock_guard<std::mutex> lk(set_clear_mutex);
//		//thread_cond = &cv;
//	}
//
//	void clear_condition_variable()
//	{
//		//std::lock_guard<std::mutex> lk(set_clear_mutex);
//		//thread_cond = 0;
//	}
//};

thread_local interrupt_flag this_thread_interrupt_flag;

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
			flag->set();
	}

	void join() { internal_thread.join(); }
	void detach() { internal_thread.detach(); }
	bool joinable() const { return internal_thread.joinable(); }

};

int main()
{
	auto F1 = [] {
		std::cout << "Start F1" << std::endl;
		int i = 0;
		try
		{
			while (true)
			{
				interruption_point();
				std::cout << "F1 Cycling : " << ++i << std::endl;
				std::this_thread::sleep_for(std::chrono::milliseconds(1000));
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
		std::this_thread::sleep_for(std::chrono::milliseconds(3000));
		T1.interrupt();
		std::cout << "Endof F2" << std::endl;
	});


	T1.join();
	T2.join();
	return 0;
}
