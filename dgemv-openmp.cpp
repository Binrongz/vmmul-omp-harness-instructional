#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <omp.h>

const char* dgemv_desc = "OpenMP dgemv.";

/*
 * This routine performs a dgemv operation
 * Y :=  A * X + Y
 * where A is n-by-n matrix stored in row-major format, and X and Y are n by 1 vectors.
 * On exit, A and X maintain their input values.
 */

void my_dgemv(int n, double* A, double* x, double* y) {

   // #pragma omp parallel
   // {
   //    // Get the total number of threads participating in this parallel region
   //    int nthreads = omp_get_num_threads();
   //    // Get the ID of the current thread (0, 1, 2, ..., nthreads-1)
   //    int thread_id = omp_get_thread_num();
   //    // 1. Determine which rows of the matrix this thread should process
   //    // Compute the starting row index (inclusive) for this thread.
   //    // Divide the total number of rows 'n' evenly among all threads.
   //    int istart = thread_id * n / nthreads;
   //    int iend = (thread_id + 1) * n / nthreads;

   //    // 2. Each thread performs the computation only on its assigned rows
   //    // Outer loop over the subset of rows assigned to this thread.
   //    for (int i = istart; i < iend; i++)
   //    {
   //       double temp = 0.0;
   //       for (int j = 0; j < n; j++)
   //       {
   //          temp += A[i * n + j] * x[j]; // A * X
   //       }
   //       y[i] += temp; // Y:= A * X + Y
   //    }
   
   //    // printf("my_dgemv(): Hello world: thread %d of %d checking in. \n", thread_id, nthreads);
   //    // printf("my_dgemv(): For actual timing runs, please comment out these printf() and omp_get_*() statements. \n");
   // }

   // insert your dgemv code here. you may need to create additional parallel regions,
   // and you will want to comment out the above parallel code block that prints out
   // nthreads and thread_id so as to not taint your timings

   #pragma omp parallel for
   for (int i = 0; i < n; i++)
   {
      double temp = 0.0;
      for (int j = 0; j < n; j++)
      {
         temp += A[i * n + j] * x[j]; // A * X
      }
      y[i] += temp; // Y:= A * X + Y
   }
}