#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

final const int MAX_SIZE;

set<int> get_possible_soluions(string word, char ch, vector<string> dictionary); 
bool update_solution(map<int, set<char>> solution, char ch, set<char> poss_solutions);
void decrypt(string* dict, string* words);

int main() {
	int n;
	
	vector<string> dictionary;
	vector<string> encrypted_words;
	
	cin >> n;

	for (int i = 0; i < n; i++) {
		
	
	}



	cout << "Hello World!" << endl;
}

void decrypt(vector<string> dictionary, vector<string> encrypted_words() {
	map<char, set<char>> solution;
	
	for (int i = 0; i < encrypted_words.size(); i++) {
		string word = encrypted_words[i];
		for (int j = 0; j < word.size(); j++) {
			set<char> poss_solutions = get_possible_solutions(word, j, dictionary);
			
			update_solution(word[j], poss_solutions, solution);
			
			// Case: Need to filter solution for character, such that
			// entire words are taken into account
			if (solution[word[j]].size() == 1):
		       			
		}
	}	
}
bool update_solution(char ch, set<char> poss_solutions, map<char, set<char>> solution) {
	if (solution.find(ch) == 0) {
		if (poss_solutions.size() == 0) {
			return false;	
		} else {
			solution[ch] = poss_solutions;
		}
	} else {
		for (int i = 0; i < poss_solutions.size(); i++) {
			if (poss_solution[i].count(solutions[ch]) == 0) {
				solution[ch].remove(poss_solutions[i]); // Method doesnt actually exist
			}
		}
		if (solution[ch].size() == 0) {
			return false;
		}
	}
	return true;
}

set<char> get_possible_solutions(string word, int ch_index, vector<string> dictionary) {
	set<char> poss_solutions;

	for (int i = 0; i < dictionary.size(); i++) {
		string dic_word = dictionary[i];
		if (word.length() == dic_word.length()):
			poss_solutions.insert(dic_word[ch_index]);
	}
	
	return poss_solutions;
}


