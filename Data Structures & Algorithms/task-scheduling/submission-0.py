class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq={}
        
        for task in tasks:
            task_freq[task]= 1+task_freq.get(task,0)
        print(task_freq)
        
        task_freq_arr_heap=[-1*freq for freq in task_freq.values()]
        print(task_freq_arr_heap)
        heapq.heapify(task_freq_arr_heap)
        
        time=0
        q= deque()

        while task_freq_arr_heap or q:
            time+=1
            if not task_freq_arr_heap:
                time= q[0][1]
            else:
                 cur_max_freq= -1*heapq.heappop(task_freq_arr_heap)-1
                 if cur_max_freq:
                    q.append([cur_max_freq,time+n])
            if q and q[0][1]==time:
                heapq.heappush(task_freq_arr_heap, -1*q.popleft()[0])
        return time
