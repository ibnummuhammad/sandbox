#include <iostream>

class MyClass
{
public:
	int num;
	void increase() { num += 5; }
};

int main(int argc, char **argv)
{
	std::cout << "argc: " << argc << std::endl;
	std::cout << "argv: " << argv << std::endl;
	return 0;
}