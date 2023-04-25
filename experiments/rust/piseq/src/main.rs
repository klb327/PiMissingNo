use std::fs;

fn main() {
    // Read the pi digits input file
    let pi_digits = fs::read_to_string("pi_digits.txt").expect("Failed to read file");

    // Define the length of the number sequence to search for
    let seq_length = 4;

    // Initialize a vector to store all number sequences of the given length
    let mut sequences = Vec::new();

    // Loop through each digit in the string, up to the second-to-last digit in order to have enough digits to form a sequence of the given length
    for i in 0..(pi_digits.len() - seq_length) {
        // Extract the number sequence of the given length
        let seq = &pi_digits[i..(i + seq_length)];

        // If the sequence consists of only digits, append it to the vector of sequences
        if seq.chars().all(char::is_numeric) {
            sequences.push(seq.to_string());
        }
    }

    // Print all the number sequences of the given length
    for seq in sequences {
        println!("{}", seq);
    }
}
