#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

final const int MAX_SIZE;

set<int> get_possible_soluions(char ch, set<string> dictionary, set<string> enc_words); 
bool update_solution(map<int, vector<int>> solution, char ch, set<int> poss_solutions);
void decrypt(string* dict, string* words);

int main() {
	int n;
	string words[MAX_SIZE];
	
	cin >> n;

	for (int i = 0; i < n; i++) {
		
	
	}

	cout << "Hello World!" << endl;
}

set<int> get_possible_solutions(char ch, set<string> dictionary, set<string> enc_words) {
	set<int> poss_solutions;
}


