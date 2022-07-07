#include "header.h"

void playGame(const int boardHeight, const int boardWidth,
		    int gameBoard[boardHeight][boardWidth])
{
    int playerNum =1;

    int playerChoice = 0;
    int changeFlag = 0;

    int full = 0;

    char player1_name[1024];
    char player2_name[1024];

    inputPlayerNames(player1_name,sizeof(player1_name), player2_name,sizeof(player2_name) );

    char inputBuffer [1024];

    while(1)
    {
        #ifdef __linux__
            system("clear");
        #elif _WIN32
            system("cls");
        #endif
        
        displayGridDefault(boardHeight,boardWidth,gameBoard );
        printf("\n\n\n");
        displayGrid(boardHeight,boardWidth,gameBoard );

        if(playerNum == 1)
            printf("%s response : ",player1_name);
        else
            printf("%s response : ",player2_name);

        fgets(inputBuffer, sizeof(inputBuffer), stdin);

        if(inputBuffer[0] >= '1' && inputBuffer[0] <= '9' && inputBuffer[1] == '\n')
        {
            inputBuffer[strlen(inputBuffer)-1] = '\0';
            playerChoice = atoi(inputBuffer);
        }
        else
        {
            continue;
        }
            
        

        changeFlag = 0;

          
        
        switch (playerChoice)
        {
            case 1:
                if(gameBoard[0][0] == -1)
                {
                    gameBoard[0][0] = playerNum % 2;
                    changeFlag = 1;
                }
                    
                break;
            case 2:
                if(gameBoard[0][1] == -1)
                {
                    gameBoard[0][1] = playerNum % 2;
                    changeFlag = 1;
                }
                    
                break;
            case 3:
                if(gameBoard[0][2] == -1)
                {
                    gameBoard[0][2] = playerNum % 2;
                    changeFlag = 1;
                }
                    
                break;
            case 4:
                if(gameBoard[1][0] == -1)
                {
                    gameBoard[1][0] = playerNum % 2;
                    changeFlag = 1;
                }
                    
                break;
            case 5:
                if(gameBoard[1][1] == -1)
                {
                    gameBoard[1][1] = playerNum % 2;
                    changeFlag = 1;
                }
                    
                break;
            case 6:
                if(gameBoard[1][2] == -1)
                {
                    gameBoard[1][2] = playerNum % 2;
                    changeFlag = 1;
                }
                    
                break;
            case 7:
                if(gameBoard[2][0] == -1)
                {
                    gameBoard[2][0] = playerNum % 2;
                    changeFlag = 1;
                }
                    
                break;
            case 8:
                if(gameBoard[2][1] == -1)
                {
                    gameBoard[2][1] = playerNum % 2;
                    changeFlag = 1;
                }
                    
                break;
            case 9:
                if(gameBoard[2][2] == -1)
                {
                    gameBoard[2][2] = playerNum % 2;
                    changeFlag = 1;
                }
                    
                break;

        default:
            printf("invalid choice try again\n");
        }

        if (changeFlag == 1)
        {
            int winner = checkForWinner(boardHeight,boardWidth,gameBoard, playerNum%2);
            
            if (winner != -1)
            {
                displayGridDefault(boardHeight,boardWidth,gameBoard );
                printf("\n\n\n");
                displayGrid(boardHeight,boardWidth,gameBoard );
                printf("\n\n\n");
                if ( winner == 1)
                    printf("Player %s is winner\n",player1_name);
                else
                    printf("Player %s is winner\n",player2_name);
                return;    
            }
            
            if(playerNum %2 == 1)
                playerNum = 2;
            else
                playerNum = 1;
            
            full++;
            if(full == 9)
            {
                displayGridDefault(boardHeight,boardWidth,gameBoard );
                printf("\n\n\n");
                displayGrid(boardHeight,boardWidth,gameBoard );
                printf("\n\n\n");
                printf("Draw\n");
                return ;
            }
        }
        
        
    } 
    
}