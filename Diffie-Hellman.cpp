#include <iostream> //input output header
#include <cmath> //math header

int PrimeChecker(int n) // Function to check if number is prime
{
    for(int i=2; i < n; i++)
    {
       if(n%i!=0)
          return 1;
       else 
          return 0;
    }  
}

int main() // main function
{

	using namespace std;
	int base, secret, modulus, uresult, b1, b2, b2s, r2s; //declare variables

	cout << "\n"; //introduction
	cout << "*********************************\n";
	cout << "*  Diffie-Hellman Key Exchange  *\n";
	cout << "*  ---------------------------  *\n";
	cout << "*    Authored by Jack Renshaw   *\n";
	cout << "*********************************\n";
	cout << "\n";

	cout << "Enter your shared prime base: "; //Request prime base from user
	cin >> base; // input base
	cout << "Enter your shared prime modulus: "; //Request prime modulus from user
	cin >> modulus; // input modulus
	cout << "Enter your secret key: "; //Request secret number from user
	cin >> secret; // input secret, must already be int

	b1 = PrimeChecker(base); //verify that base is prime
	b2 = PrimeChecker(modulus); // verify that modulus is prime

	if(b1 != 1){
		cout << "Your base is not prime...\n"; //return error
	}
	if(b2 != 1){
		cout << "Your modulus is not prime...\n"; //return error
	}

	b2s = pow(base, secret); // calculate the base to the power of secret

	cout << "Share this result with your partner: " << b2s % modulus << endl << endl; // Return result
	cout << "Enter your partners result: "; // Request partners result
	cin >> uresult; // input result

	r2s = pow(uresult, secret); // calculate the parter result to the power of secret
	cout << "Your shared secret is: " << r2s % modulus << endl << endl; // Return shared key

	cout << "Congratulations, you can now communicate in secret" << endl << endl; // Finnito

	return 0;

}