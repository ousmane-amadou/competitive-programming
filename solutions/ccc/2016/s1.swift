var word1 : String
var word2 : String

word1 = readLine()!
word2 = readLine()!

func isAnagram(word1: String, word2: String) -> Bool {
    if(word1.count != word2.count) {
      return false
    }

    var charCount = [Character : Int]()

    // Records the number of occurrences of each character in word1
    for character in word1 {
        let numOccr = charCount[character] ?? 0
        charCount[character] =  numOccr + 1
    }

    // Checks whether each character reappears in word2 or whther
    // each character has a corresponding '*'.

    for character in word2 {
      if (charCount[character] == 0 || charCount[character] == nil) && (character != "*")  {
        return false
      } else {
        let numOccr = charCount[character] ?? 0
        charCount[character] =  numOccr - 1
      }
    }
    return true
}
if isAnagram(word1: word1, word2: word2) {
  print("Y")
} else {
  print("N")
}
