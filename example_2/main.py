import sys


source_code = """#include <iostream>

int main() {
    std::cout << "hello, example_2" << std::endl;
    return 0;
}

"""

gen_filename = sys.argv[1]

print('gen_filename', gen_filename)

open(gen_filename, 'w').write(source_code)
