
#include "header.h"
void resetGameBoard(const int boardHeight, const int boardWidth,
		    int gameBoard[boardHeight][boardWidth])
{
    for(int i=0; i < boardHeight; i++)
    {
        for(int j=0; j < boardWidth;j++)
		gameBoard[i][j] = -1;
    }
}
