#include <pybind11/pybind11.h>

namespace py = pybind11;

// C++ wrapper for the Swift function
extern "C" {
    int add(int a, int b);
    void say_hi();
    const char * get_result(int num1, int num2);
}

std::string get_result_as_string(int num1, int num2){
    auto result = get_result(num1, num2);
    auto result_string = std::string(result);
    free((void*) result);
    return result_string;
}

PYBIND11_MODULE(mymodule, m) {
    m.def("add", &add, "A function that adds two numbers");
    m.def("say_hi", &say_hi, "A function that adds two numbers");
    m.def("get_result", [](int num1, int num2){return get_result_as_string(num1, num2);}, "get the result");
}
