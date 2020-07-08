#include<iostream>
#include<vector>
#include <algorithm>
#include "helpers.cpp"

using namespace std;

int main(){

    char color,
	vector< vector <char> > grid,
	vector< vector <float> > beliefs,
	float p_hit,
	float p_miss)
{
	int height = grid.size();
    int width  = grid[0].size();
	vector< vector <float> > newGrid = zeros(height,width);

	float new_prob;
	for (int row=0; row<height; ++row){
	    for (int col=0; col<width; ++col){
           if(grid[row][col]==color){
                new_prob = beliefs[row][col]*p_hit;
                newGrid[row][col] = new_prob;
           }
           else{
                new_prob = beliefs[row][col]*p_miss;
                newGrid[row][col] = new_prob;
           }
	    }
	}

	int height = grid.size();
	int width = grid[0].size();
	float normalizer = 0.0;
	vector< vector<float> > newGrid = zeros(height,width);

	for (int row=0; row<height; ++row){
	    for (int col=0; col<width; ++col){
                normalizer += grid[row][col];
	    }
	}

	for (int row=0; row<height; ++row){
	    for (int col=0; col<width; ++col){
            newGrid[row][col] = grid[row][col] / normalizer;
	    }
	}

    return 0;
}
