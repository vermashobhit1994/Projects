#include "header.h"
int checkForWinner(const int heightGameBoard, 
                     const int widthGameBoard, 
					 int gameBoard[heightGameBoard][widthGameBoard],
                     const int playerNum)
{
    if(playerNum == gameBoard[0][0] && playerNum == gameBoard[0][1] && playerNum == gameBoard[0][2] || //first row
       playerNum == gameBoard[1][0] && playerNum == gameBoard[1][1] && playerNum == gameBoard[1][2] || //second row
       playerNum == gameBoard[2][0] && playerNum == gameBoard[2][1] && playerNum == gameBoard[2][2] || //third row
       playerNum == gameBoard[0][0] && playerNum == gameBoard[1][0] && playerNum == gameBoard[2][0] || //first column
       playerNum == gameBoard[0][1] && playerNum == gameBoard[1][1] && playerNum == gameBoard[2][1] || //second column
       playerNum == gameBoard[0][2] && playerNum == gameBoard[1][2] && playerNum == gameBoard[2][2] || //third column
       playerNum == gameBoard[0][0] && playerNum == gameBoard[1][1] && playerNum == gameBoard[2][2] || //diagonal 1
       playerNum == gameBoard[0][2] && playerNum == gameBoard[1][1] && playerNum == gameBoard[2][0] 
    )
        return playerNum;
    return -1;
}
