import numpy as np

def single_queue_simulation(arrival_mean, arrival_std, service_min, service_max, num_customers, seed=None):
    np.random.seed(seed)
    
    
    #توزیع نرمال
    interarrival_times = np.random.normal(arrival_mean, arrival_std, num_customers)
    
    #توزیع یکنواخت
    service_times = np.random.uniform(service_min, service_max, num_customers)

    arrival_times = np.cumsum(interarrival_times)
    service_start_times = np.zeros(num_customers)
    wait_times = np.zeros(num_customers)
    service_end_times = np.zeros(num_customers)

    for i in range(1, num_customers):
        service_start_times[i] = max(arrival_times[i], service_end_times[i-1])
        wait_times[i] = service_start_times[i] - arrival_times[i]
        service_end_times[i] = service_start_times[i] + service_times[i]

    queue_wait_time = np.mean(wait_times)
    server_idle_time = np.sum(service_start_times[1:] - service_end_times[:-1]) / service_end_times[-1]

    return queue_wait_time, server_idle_time

# پارامترهای ورودی
arrival_mean = 5   # میانگین زمان ورود به صف
arrival_std = 2    # انحراف معیار زمان ورود به صف
service_min = 3    # حداقل زمان خدمت دهی
service_max = 7    # حداکثر زمان خدمت دهی
num_customers = 20  # تعداد مشتریان

queue_wait_time, server_idle_time = single_queue_simulation(arrival_mean, arrival_std, service_min, service_max, num_customers)

print(f"مدت زمان انتظار در صف: {queue_wait_time:.2f} واحد زمان")
print(f"مدت بیکاری خدمت‌دهنده: {server_idle_time:.2f} واحد زمان")

