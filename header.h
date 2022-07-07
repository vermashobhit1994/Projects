#ifndef __HEADER_H__
#define __HEADER_H__
#include <stdio.h>

#include<stdlib.h>//system()

#include<string.h>
typedef enum 
{
    PRINT_GRID_DEFAULT_NUM,
    PRINT_GRID_GAME_ARRAY,
    PRINT_GRID_DEFAULT_CHAR,
    PRINT_GRID_EMPTY,
}PRINT_GRID;

void displayGridDefault(const int heightGameBoard, 
                     const int widthGameBoard, 
					 int gameBoard[heightGameBoard][widthGameBoard]);

void displayGrid(const int heightGameBoard, 
                     const int widthGameBoard, 
					 int gameBoard[heightGameBoard][widthGameBoard]);

void resetGameBoard(const int boardHeight, const int boardWidth,
		    int gameBoard[boardHeight][boardWidth]);

void playGame(const int boardHeight, const int boardWidth,
		    int gameBoard[boardHeight][boardWidth]);

int checkForWinner(const int heightGameBoard, 
                     const int widthGameBoard, 
					 int gameBoard[heightGameBoard][widthGameBoard],
                     const int playerNum);

void inputPlayerNames(char* player1_name, size_t player1_length, char* player2_name, 
                     size_t player2_length);


#endif
