#include "header.h"


void inputPlayerNames(char* player1_name, size_t player1_length, char* player2_name, 
                     size_t player2_length)
{
    printf("Player1 name: ");
    fgets(player1_name, player1_length,stdin);
    player1_name[strlen(player1_name)-1] = '\0';

    printf("Player2 name: ");
    fgets(player2_name, player2_length,stdin);
    player2_name[strlen(player2_name)-1] = '\0';

}

