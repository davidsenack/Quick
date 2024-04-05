#include<stdio.h>
#include<gmp.h>

void fibonacci(mpz_t result, mpz_t n) {
    if (mpz_cmp_ui(n, 1) <= 0) {
        mpz_set(result, n);
    } else {
        mpz_t n_minus_1;
        mpz_init(n_minus_1);
        mpz_sub_ui(n_minus_1, n, 1);
        mpz_t n_minus_2;
        mpz_init(n_minus_2);
        mpz_sub_ui(n_minus_2, n, 2);

        mpz_t fib_n_minus_1;
        mpz_init(fib_n_minus_1);
        fibonacci(fib_n_minus_1, n_minus_1);

        mpz_t fib_n_minus_2;
        mpz_init(fib_n_minus_2);
        fibonacci(fib_n_minus_2, n_minus_2);

        mpz_add(result, fib_n_minus_1, fib_n_minus_2);

        mpz_clear(n_minus_1);
        mpz_clear(n_minus_2);
        mpz_clear(fib_n_minus_1);
        mpz_clear(fib_n_minus_2);
    }
}

int main(void) {
    mpz_t n;
    mpz_init_set_ui(n, 10); // Set n to the value for which Fibonacci is calculated
    mpz_t result;
    mpz_init(result);

    fibonacci(result, n);

    gmp_printf("%Zd\n", result);

    mpz_clear(n);
    mpz_clear(result);
    return 0;
}