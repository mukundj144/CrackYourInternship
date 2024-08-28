class Solution:

    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, n):
        # Step 1: Sort jobs by profit in descending order.
        Jobs.sort(key=lambda x: x.profit, reverse=True)

        # Step 2: Find the maximum deadline among the jobs.
        max_deadline = max(job.deadline for job in Jobs)

        # Step 3: Create a slot array to keep track of used time slots.
        slot = [-1] * (max_deadline + 1)

        # Initialize counters for the number of jobs done and total profit.
        count_jobs = 0
        total_profit = 0

        # Step 4: Iterate through all jobs to find a slot.
        for job in Jobs:
            # Find a free slot for this job (starting from its deadline).
            for j in range(job.deadline, 0, -1):
                if slot[j] == -1:
                    slot[j] = job.id  # Assign this job to the slot.
                    count_jobs += 1
                    total_profit += job.profit
                    break

        # Step 5: Return the number of jobs done and the total profit.
        return count_jobs, total_profit