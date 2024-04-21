#include <iostream>

class A {
public:
  virtual void display() { std::cout << "Base class is invoked" << std::endl; }
};

class B : public A {
public:
  void display() { std::cout << "Derived Class is invoked" << std::endl; }
};

int main() {
  A *a; // pointer of base class
  B b;  // object of derived class
  a = &b;
  a->display(); // Late Binding occurs
}