



#include "header.h"


//private function  
static void displayGridAndBoundary(const int heightGameBoard, 
                     const int widthGameBoard, 
					 int gameBoard[heightGameBoard][widthGameBoard], 
					 PRINT_GRID printGridChar);



static int check_num_pairs(int i, int j, 
                     int height, 
		 int width,
		 int underscore_per_block,
		 int star_per_row,
		 int star_per_block)
{
    int num = 0;
    int first_block_row = (height-1)/4;
    int first_block_col =( width-1) /4;

    if (i == first_block_row && j == first_block_col)
	    num = 1;
    else if ( i == first_block_row && j == (first_block_col + underscore_per_block+star_per_row/2) )
	    num = 2;
    else if ( i == first_block_row && j == (first_block_col + 2*underscore_per_block + star_per_row  ) )
	    num = 3;
    else if ( (i == first_block_row + star_per_block) && j == first_block_col)
	    num = 4;
    else if ( (i == first_block_row + star_per_block) && j == (first_block_col + underscore_per_block + star_per_row/2) )
	    num = 5;
    else if ( (i == first_block_row + star_per_block) && j == (first_block_col + 2*underscore_per_block + star_per_row))
	    num = 6;
    else if ( (i == first_block_row + 2*star_per_block) && (j == first_block_col) )
	    num = 7;
    else if ( (i == first_block_row + 2*star_per_block)  && (j == first_block_col + underscore_per_block + star_per_row/2) )
	    num = 8;
    else if ( (i == first_block_row + 2*star_per_block) && (j == first_block_col + 2*underscore_per_block + star_per_row) )
	    num = 9;
    else
	    num = 0;
    return num;
}

static void printGameArray(int row, int cols, int gameArray[row][cols], int position)
{
    
	int gameGridValue = 0; 
    switch(position)
    {
    case 1:
	    gameGridValue = gameArray[0][0];
	    break;
	case 2:
	    gameGridValue = gameArray[0][1];
	    break;
	case 3:
	    gameGridValue = gameArray[0][2];
	    break;
	case 4:
	    gameGridValue = gameArray[1][0];
	    break;
	case 5:
	    gameGridValue = gameArray[1][1];
	    break;
	case 6:
	    gameGridValue = gameArray[1][2];
	    break;
	case 7:
	    gameGridValue = gameArray[2][0];
	    break;
	case 8:
	    gameGridValue = gameArray[2][1];
	    break;
	case 9:
	    gameGridValue = gameArray[2][2];
	    break;
	default:

    }
    if(position >=1 && position <= 9)
	{
        if(gameGridValue == 0)
			printf("%c",'O');
		else if (gameGridValue == 1)
		    printf("%c",'X');
		else 
		    printf(" ");
	}
	
	    
}

void displayGridDefault(const int heightGameBoard, 
                     const int widthGameBoard, 
					 int gameBoard[heightGameBoard][widthGameBoard])
{
	displayGridAndBoundary(heightGameBoard, widthGameBoard,gameBoard,
	            PRINT_GRID_DEFAULT_NUM);	
}

void displayGrid (const int heightGameBoard, 
                     const int widthGameBoard, 
					 int gameBoard[heightGameBoard][widthGameBoard])
{
	displayGridAndBoundary(heightGameBoard, widthGameBoard,gameBoard,
	            PRINT_GRID_GAME_ARRAY);
}

static void displayGridAndBoundary(const int heightGameBoard, 
                     const int widthGameBoard, 
					 int gameBoard[heightGameBoard][widthGameBoard], 
					 PRINT_GRID printGridChar
					 )
{
    const int height = 13;
    const int width = 26;

    //int height = 13-1;
    //int width = 26-1;


    int star_per_row = 2;
    int star_per_block = 3;
    int space_per_first_block = ( (width-1) /5 -1);
    int space_per_last_block = space_per_first_block -1;
    
    int underscore_per_block = ((width-1) - (space_per_first_block + space_per_last_block) -star_per_row) /3;

    int first_underscore_start = (width-1)/6;
    int second_underscore_start = first_underscore_start + underscore_per_block +1;
    int third_underscore_start =  second_underscore_start + underscore_per_block + 1 ;

    int first_star_start = (width-1)/3+1;
    int second_star_start = first_star_start + underscore_per_block +1;  
    
    int setGridMargin = 20;

    int num = 0;

    const char defaultChar = '@';
    

    for(int i=0; i < height;i++)
    {
	if (setGridMargin > 0)
	    printf("%*c",setGridMargin, ' ');

    	for(int j=0; j < width;j++)
		{
			if( (i % (height-1)) == 0 )
				printf("-");
			else if( (i % (height-1) != 0) &&  ( (j % (width-1)) == 0) )
				printf("+");
			else if ( (i == (height-1)/3 || i == (height-1)/3 + star_per_block)   && 
				( j == first_underscore_start || j == second_underscore_start ||  j == third_underscore_start  ) )
				{
			int start = j;
					while ( start <= j+(underscore_per_block-1) )
			{
				printf("_");
				start++;
			
			}
			j+= (underscore_per_block-1);
				
			} 
			else if ( (num = check_num_pairs (i,j,height, 
								width,underscore_per_block,
								star_per_row,star_per_block) ) != 0)
			{
				switch(printGridChar)
				{
					case PRINT_GRID_DEFAULT_CHAR:
						printf("%c",defaultChar);
						break;
					case PRINT_GRID_DEFAULT_NUM:
						printf("%d",num);
						break;
					case PRINT_GRID_GAME_ARRAY:
						printGameArray(heightGameBoard,widthGameBoard,
										gameBoard,num);
						break;
					default:
						printf(" ");

				}
			}
			else if ( (j == first_star_start || j == second_star_start) && 
				(i >= 2 && i <= star_per_block*3+1) )
			{
				printf("*");
			} 
			else
				printf(" ");
		}
	printf("\n");
    }
}
