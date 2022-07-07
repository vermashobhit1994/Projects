
#include "header.h"
#include <stdio.h>
#include <string.h> //bzero()
int main()
{
	size_t heightGameBoard= 3;
	size_t widthGameBoard = 3;

	int gameBoard[heightGameBoard][widthGameBoard] ;
	resetGameBoard(heightGameBoard, widthGameBoard,gameBoard);
	
	
	

	playGame(heightGameBoard,widthGameBoard, gameBoard);
    
}
