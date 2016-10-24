/*
 *    $$\   $$\  $$$$$$\  $$$$$$\ $$\   $$\ $$\   $$\       $$$$$$$\             $$$$$$\  
 *    $$$\  $$ |$$  __$$\ \_$$  _|$$$\  $$ |$$ |  $$ |      $$  __$$\           $$  __$$\ 
 *    $$$$\ $$ |$$ /  \__|  $$ |  $$$$\ $$ |\$$\ $$  |      $$ |  $$ | $$$$$$\  $$ /  \__|
 *    $$ $$\$$ |$$ |$$$$\   $$ |  $$ $$\$$ | \$$$$  /       $$ |  $$ |$$  __$$\ \$$$$$$\  
 *    $$ \$$$$ |$$ |\_$$ |  $$ |  $$ \$$$$ | $$  $$<        $$ |  $$ |$$ /  $$ | \____$$\ 
 *    $$ |\$$$ |$$ |  $$ |  $$ |  $$ |\$$$ |$$  /\$$\       $$ |  $$ |$$ |  $$ |$$\   $$ |
 *    $$ | \$$ |\$$$$$$  |$$$$$$\ $$ | \$$ |$$ /  $$ |      $$$$$$$  |\$$$$$$  |\$$$$$$  |
 *    \__|  \__| \______/ \______|\__|  \__|\__|  \__|      \_______/  \______/  \______/ 
 *                                                                                        
 *                                                                                        
 *                                                                                        
 *
 *             /!\ Welcome to the scanner of NGINX DoS /!\
 *
 *                    #1.) Install gcc
 *                     apt-get install gcc
 *                     yum install gcc
 *
 *                    #2.) Compile with gcc
 *                  gcc -pthread scanner.c -o scanner
 *
 *                    #3.) Usage
 *                     ./scanner amount
 *                     ./scanner 500
 *
 *                    #4.) Copy & Paste
 *                     copy gnix servers
 *                   paste inside of gnix.txt
 *
 *                    #5.) DDoS usage
 *              redirect to ddos.py for usage on nginx.txt
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define DELIMIT ", "

int main(int argc, char **argv)
{
    int ipnum;

    if(argc < 2)
    {
        printf("Usage: %s 50\n", *argv);
        return 1;
    }

    ipnum = atoi(argv[1]);

    srand(time(NULL));

    while(ipnum--)
    {
       unsigned int ipaddr = ~rand();
       printf("%u.%u.%u.%u"DELIMIT, (ipaddr >> 24), (ipaddr >> 16) & 0xFF, (ipaddr >> 8) & 0xFF, ipaddr & 0xFF);
    }
    putchar(10);

    return 0;
}
