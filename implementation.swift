import Foundation

@_cdecl("add")
public func add(a: Int, b: Int) -> Int {
    return a + b
}

@_cdecl("say_hi")
public func say_hi() {
    print("Hi!")
}

private struct Result {
    let a: Int32
    let b: Int32
    let c: Int32

     init(a: Int32, b: Int32, c: Int32) {
        self.a = a
        self.b = b
        self.c = c
    }
}

@_cdecl("get_result")
public func get_result(num1: Int32, num2: Int32) -> UnsafePointer<CChar> {
    // Create internal struct
    let result = Result(a: num1, b: num2, c: num1 + num2);

    // Convert to JSON
    let json_data_string = "{\"data\" : [\(result.a), \(result.b), \(result.c)]}"
    let json = json_data_string.utf8.map{CChar($0)}  + [CChar(exactly:"\0".utf8.first!)!]

    // Allocate memory for an array of length of the string
    let count = json.count
    let pointer = UnsafeMutablePointer<CChar>.allocate(capacity: count)

    // Copy data into UnsafeMutablePointer
    for (ind, char) in json.enumerated() {
        pointer[ind] = char
    }
    return UnsafePointer(pointer)
}


