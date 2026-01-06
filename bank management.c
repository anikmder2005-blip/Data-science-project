#include <stdio.h>
#include <stdlib.h>

struct account {
    int acc_no;
    char name[50];
    float balance;
};

void createAccount();
void displayAccount();
void deposit();
void withdraw();

int main() {
    int choice;

    while (1) {
        printf("\n====== BANKING MANAGEMENT SYSTEM ======\n");
        printf("1. Create Account\n");
        printf("2. Display Account\n");
        printf("3. Deposit Money\n");
        printf("4. Withdraw Money\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
        case 1:
            createAccount();
            break;
        case 2:
            displayAccount();
            break;
        case 3:
            deposit();
            break;
        case 4:
            withdraw();
            break;
        case 5:
            exit(0);
        default:
            printf("Invalid choice!\n");
        }
    }
    return 0;
}

void createAccount() {
    struct account a;
    FILE *fp;

    fp = fopen("bank.dat", "ab");

    printf("Enter Account Number: ");
    scanf("%d", &a.acc_no);
    printf("Enter Name: ");
    scanf("%s", a.name);
    printf("Enter Initial Balance: ");
    scanf("%f", &a.balance);

    fwrite(&a, sizeof(a), 1, fp);
    fclose(fp);

    printf("Account created successfully!\n");
}

void displayAccount() {
    struct account a;
    int acc;
    FILE *fp;

    fp = fopen("bank.dat", "rb");
    printf("Enter Account Number: ");
    scanf("%d", &acc);

    while (fread(&a, sizeof(a), 1, fp)) {
        if (a.acc_no == acc) {
            printf("\nAccount Number: %d", a.acc_no);
            printf("\nName: %s", a.name);
            printf("\nBalance: %.2f\n", a.balance);
            fclose(fp);
            return;
        }
    }
    fclose(fp);
    printf("Account not found!\n");
}

void deposit() {
    struct account a;
    int acc;
    float amt;
    FILE *fp;

    fp = fopen("bank.dat", "rb+");
    printf("Enter Account Number: ");
    scanf("%d", &acc);

    while (fread(&a, sizeof(a), 1, fp)) {
        if (a.acc_no == acc) {
            printf("Enter Amount to Deposit: ");
            scanf("%f", &amt);
            a.balance += amt;

            fseek(fp, -sizeof(a), SEEK_CUR);
            fwrite(&a, sizeof(a), 1, fp);
            fclose(fp);

            printf("Amount deposited successfully!\n");
            return;
        }
    }
    fclose(fp);
    printf("Account not found!\n");
}

void withdraw() {
    struct account a;
    int acc;
    float amt;
    FILE *fp;

    fp = fopen("bank.dat", "rb+");
    printf("Enter Account Number: ");
    scanf("%d", &acc);

    while (fread(&a, sizeof(a), 1, fp)) {
        if (a.acc_no == acc) {
            printf("Enter Amount to Withdraw: ");
            scanf("%f", &amt);

            if (amt > a.balance) {
                printf("Insufficient balance!\n");
            } else {
                a.balance -= amt;
                fseek(fp, -sizeof(a), SEEK_CUR);
                fwrite(&a, sizeof(a), 1, fp);
                printf("Withdrawal successful!\n");
            }
            fclose(fp);
            return;
        }
    }
    fclose(fp);
    printf("Account not found!\n");
}
