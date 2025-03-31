#include <stdio.h>
#include <string.h>

int encrypt_key(char *key) 
{
    int key_length = strlen(key);
    int key_sum = 0;
    for (int i = 0; i < key_length; i++) {
        key_sum += key[i];
    }
    return key_sum * key_length;
}

void two_fa() {
    printf("\nSorry, ever since our flag got leaked. We have to do a second layer of checks now. \nPlease enter your personalized authentication code: ");
    char key[16];
    scanf("%15s", key); 
    if ( 1804 == encrypt_key( key ) ) {
        FILE *fp = fopen("flag.txt", "r");
        if (fp == NULL) { 
            printf("Error: failed to open flag file\n");
            return;
        }
        char flag[64];
        fgets(flag, 64, fp);
        printf("Congratulations! Here is your flag: %s", flag);
        fclose(fp);
    } else {
        printf("Wrong key!\n");
    }
}

int main()
{
    FILE *fp = fopen("flag.txt", "r");
    if ( fp == NULL ) { 
        printf("Error: failed to open flag file\n");
        return 1;
    }
    char flag[64];
    fgets(flag, 64, fp);
    fclose(fp); 
    int authorization = 0;
    char secret[6];
    printf("Welcome to the alien portal!\n");
    printf("What is your password?: ");
    gets(secret);
    if( strcmp ( secret, flag ) == 0 ) {
        authorization = 1;
    }
    if ( authorization == 1 ) {
        two_fa();
    } else {
        printf("Intruder Alert!\n");
        return 0;
    }
}