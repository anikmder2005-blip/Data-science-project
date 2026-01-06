
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main (){
    int random, Guess;
    int no_of_guess=0;
    srand(time(NULL));


    printf("welcome to the world of guessing numbers\n");
    random = rand () % 100 + 1;

    do {
        printf("\nplease enter your guessing between(1 to 100):");
        scanf("%d", &Guess);
        no_of_guess++;

        if(Guess < random){
            printf("Guess a larger number.\n");
        } else if (Guess > random){
            printf("Guess a smaller number. \n");
        } else {
            printf("congratulations !!!you have sucessfully guessed the number in %d attempts", no_of_guess);
        }

    } while (Guess !=random);

    printf("\n bye bye, thanks for playing.");
    printf("\n developed by: anik");
}