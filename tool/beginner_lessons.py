"""Beginner onboarding, original examples and reference solutions."""
GUIDES = {}
def guide(id, terms, before, code, trace, question, options, answer, task, hint, solution, result):
    GUIDES[id] = dict(terms=terms, before=before, code=code, trace=trace, question=question, options=options, answer=answer, task=task, hint=hint, solution=solution, result=result)

guide('python', ['Program: a sequence of instructions a computer follows.', 'String: text enclosed in quotes.', 'Variable: a name that refers to a value.', 'Output: the result a program displays.'],
 'No programming experience is needed. Open Code lab. Replace its sample with the two lines below. Type straight quotes, not decorative quotation marks. Press Run code. You can also trace the example on paper.',
 'name = "Salam"\nprint(name)',
 ['Line 1 stores the string Salam under the name name. The equals sign assigns a value; it does not ask a question.', 'Line 2 reads that value and displays Salam. The quotes and variable name are not printed.', 'Change Salam to Kabul and run again. Only the displayed word changes.'],
 'What will print(name) display after name = "Salam"?', ['Salam', 'name', 'Nothing'], 0,
 'Store Kabul in a variable named city, then display city on one line.', 'Replace both uses of name with city. Keep the text inside quotes.', 'city = "Kabul"\nprint(city)', 'Kabul')
guide('web-design', ['HTML: markup that gives a document structure.', 'Element: a piece of a page, usually marked by opening and closing tags.', 'Heading: a title that describes the following content.', 'Browser: the application that displays a web document.'],
 'No programming experience is needed. Create a folder named first-page. In a plain-text editor save a file named index.html, not index.html.txt. Paste the example, save it, and open it in a browser. No internet is needed.',
 '<!doctype html>\n<html lang="en">\n  <h1>School library</h1>\n  <p>Open today</p>\n</html>',
 ['The doctype asks the browser to use modern HTML rules.', 'The h1 tags mark the main heading; they are not visible text.', 'The p tags mark a paragraph. Edit Open today, save the file, then refresh the browser.'],
 'Which element marks the main heading?', ['p', 'h1', 'html'], 1,
 'Create a page with the heading My first page and a paragraph reading I can learn.', 'Keep the tags in pairs and change the text between them.', '<!doctype html>\n<html lang="en">\n<h1>My first page</h1>\n<p>I can learn.</p>\n</html>', 'The browser shows My first page as a heading and I can learn. as a paragraph.')
guide('web-development', ['Client: the program that asks for a resource.', 'Server: the program that receives and answers a request.', 'HTTP: a set of rules for web requests and responses.', 'Status: a number describing the result of a request.'],
 'First complete Web Design, JavaScript, NodeJs, and ExpressJs. If these words are new, open the prerequisites below. This first example is a paper trace; it does not require a running server.',
 'Client: GET /books\nServer: 200 OK\nBody: [{"title":"Algorithms"}]',
 ['The client asks for the resource named /books.', 'The server reports 200 to indicate success.', 'The response body carries data. The browser still needs instructions to render that data on a page.'],
 'Which participant sends the response?', ['The server', 'The CSS file', 'The keyboard'], 0,
 'Write a request and a successful response for a local /courses resource with one course.', 'Use the same three-part trace and change the resource and JSON data.', 'Client: GET /courses\nServer: 200 OK\nBody: [{"title":"Python"}]', 'A request, a success status, and a JSON array containing one course are present.')
guide('java', ['Source file: a text file containing program instructions.', 'Compiler: a tool that checks and translates source code.', 'Method: a named group of instructions.', 'println: a method that displays a value followed by a new line.'],
 'No prior programming is required. A classroom computer needs an installed JDK. Save the example as Main.java. In that folder run javac Main.java, then java Main. Keep capital letters exactly as shown.',
 'public class Main {\n  public static void main(String[] args) {\n    System.out.println("Salam");\n  }\n}',
 ['Main is the class name and matches the file name. The outer braces enclose the class.', 'main is the entry method Java starts. Its braces enclose the instructions.', 'println displays Salam. The semicolon ends this statement. Do not delete the surrounding structure yet.'],
 'Which text is displayed by this program?', ['Main.java', 'Salam', 'String[]'], 1,
 'Change the program so it displays Kabul instead of Salam.', 'Only change the characters inside the quoted string.', 'public class Main {\n  public static void main(String[] args) {\n    System.out.println("Kabul");\n  }\n}', 'Kabul')
guide('kotlin', ['Function: a named group of instructions.', 'main: the starting function of this example.', 'val: a binding that cannot be reassigned.', 'String: a text value enclosed in quotes.'],
 'No prior programming is required. On a provisioned computer save Main.kt. Compile with kotlinc Main.kt -include-runtime -d main.jar, then run java -jar main.jar. The app cannot run Kotlin code.',
 'fun main() {\n  val city = "Kabul"\n  println(city)\n}',
 ['fun introduces a function. The braces surround its body.', 'val gives the text Kabul a name, city.', 'println reads city and displays Kabul. It does not print the word city.'],
 'What is the value referred to by city?', ['println', 'Kabul', 'main'], 1,
 'Use a val named greeting to display Salam.', 'Change the binding name and the quoted value, then update println.', 'fun main() {\n  val greeting = "Salam"\n  println(greeting)\n}', 'Salam')
guide('android', ['Activity: an Android entry point for a user interaction.', 'Composable: a function that describes part of a Compose interface.', 'State: data that determines what the interface displays.', 'Emulator: software that simulates an Android device.'],
 'Complete Kotlin first. Use a provisioned Android Studio Empty Activity project with Compose. Keep the generated project structure. Replace only the starter greeting composable with the example. Run on a prepared emulator or device.',
 '@Composable\nfun Greeting() {\n  Text("Salam")\n}\n// Call Greeting() inside the generated setContent block.',
 ['The annotation marks a Compose UI function.', 'Greeting describes one small part of the screen.', 'Text displays Salam. Text and Composable require the imports supplied by the Compose project. This fragment is not a standalone Kotlin file.'],
 'What does Text("Salam") describe?', ['A database table', 'Visible text', 'A network download'], 1,
 'Change the greeting so the screen displays Welcome.', 'Keep the composable function and change the string passed to Text.', '@Composable\nfun Greeting() {\n  Text("Welcome")\n}', 'The app screen displays Welcome.')
guide('ios', ['Scene: one instance of an app interface.', 'View: a description of visible interface content.', 'SwiftUI: Apple’s declarative interface framework.', 'Simulator: a tool for running a simulated device on a Mac.'],
 'Complete Swift first. Use a compatible Mac with provisioned Xcode. Create an iOS SwiftUI app. Replace the generated ContentView with this example and run the prepared simulator. This cannot be compiled on an Android phone.',
 'import SwiftUI\nstruct ContentView: View {\n  var body: some View {\n    Text("Salam")\n  }\n}',
 ['The import makes SwiftUI types available.', 'ContentView conforms to View and supplies a body.', 'The body describes one text element. Xcode’s generated app entry point displays ContentView.'],
 'What is displayed by the view?', ['Salam', 'ContentView.swift', 'import SwiftUI'], 0,
 'Display Welcome using the same view structure.', 'Change only the string inside Text.', 'import SwiftUI\nstruct ContentView: View {\n  var body: some View { Text("Welcome") }\n}', 'The simulator displays Welcome.')
guide('swift', ['let: a constant binding.', 'Variable: a named value that can change when declared with var.', 'String: text enclosed in quotes.', 'print: a function that displays a value.'],
 'No programming experience is required. On a computer with Swift provisioned, save main.swift and run swift main.swift from its folder. This language lesson does not require an iOS interface.',
 'let city = "Kabul"\nprint(city)',
 ['let creates a binding named city containing a string.', 'print reads city and displays its value.', 'Trying to assign another value to city later fails because this binding uses let. Use var only when reassignment is required.'],
 'Which word declares the constant binding?', ['print', 'let', 'city'], 1,
 'Declare greeting as a constant and display Salam.', 'Keep let, choose a new name, and pass that name to print.', 'let greeting = "Salam"\nprint(greeting)', 'Salam')
guide('cpp', ['Header: a declaration file included before compilation.', 'main: the function where this program begins.', 'Stream: a sequence of input or output data.', 'Statement: one instruction, often ending with a semicolon.'],
 'No prior programming is required. Use a provisioned C++ compiler. Save main.cpp and compile with g++ -std=c++17 -Wall -Wextra main.cpp -o app. Run ./app, or app.exe on Windows. The app itself cannot compile C++.',
 '#include <iostream>\nint main() {\n  std::cout << "Salam" << "\\n";\n  return 0;\n}',
 ['iostream declares standard input and output facilities.', 'main contains the program statements between braces.', 'cout sends Salam and a newline to the output. return 0 reports successful completion to the operating system.'],
 'Which expression sends text to standard output?', ['std::cout', '#include', 'return 0'], 0,
 'Display Kabul followed by a newline.', 'Replace Salam inside the quotes; keep the stream operators and semicolon.', '#include <iostream>\nint main() {\n  std::cout << "Kabul" << "\\n";\n  return 0;\n}', 'Kabul')
guide('javascript', ['Script: instructions executed by a JavaScript runtime.', 'const: a binding that cannot be reassigned.', 'Console: a developer tool that displays messages.', 'Expression: code that produces a value.'],
 'Begin with Web Design so you can create local files. Open a browser’s developer tools and its Console. Enter the two lines below. No website account or internet service is needed.',
 'const amount = 20;\nconsole.log(amount + 5);',
 ['const gives the number 20 the name amount.', 'The addition expression calculates 25 before console.log displays it.', 'The semicolon ends a statement. Numbers are not quoted here; quoted values would be strings.'],
 'What number does the example display?', ['20', '5', '25'], 2,
 'Store 30 in price and display price plus 10.', 'Use a numeric value without quotes and pass the addition expression to console.log.', 'const price = 30;\nconsole.log(price + 10);', '40')
guide('reactjs', ['Component: a reusable function describing interface content.', 'JSX: syntax for describing elements inside JavaScript.', 'Prop: an input passed to a component.', 'Render: calculate the interface description from data.'],
 'Complete JavaScript first. Open a provisioned local React starter project. In its App.jsx file use this example, keeping the project’s generated entry point. Run the starter project’s documented local command.',
 'export default function App() {\n  return <h1>Salam</h1>;\n}',
 ['App is a JavaScript function used as a component.', 'The returned JSX describes a heading containing Salam.', 'export default allows the starter entry point to import this component. JSX needs the project’s build tools and is not ordinary HTML pasted into a browser console.'],
 'What does this component return?', ['A heading description', 'A database connection', 'A Python function'], 0,
 'Return a heading containing Welcome.', 'Change only the text between the h1 tags.', 'export default function App() {\n  return <h1>Welcome</h1>;\n}', 'The local React page shows a Welcome heading.')
guide('reactnative', ['Native component: an interface element provided by the mobile platform.', 'View: a container for native layout.', 'Text: a native component used to display text.', 'Prop: an input supplied to a component.'],
 'Complete ReactJs first. Open a fully provisioned local React Native starter project. Replace its App component with this example. Use the starter’s native build command and prepared emulator; a cloud build is not required.',
 'import {View, Text} from "react-native";\nexport default function App() {\n  return <View><Text>Salam</Text></View>;\n}',
 ['The import brings native components into this module.', 'View contains the Text component.', 'Visible words belong inside Text. Browser elements such as h1 are not native components here.'],
 'Which component displays the word Salam?', ['View', 'Text', 'h1'], 1,
 'Display Welcome inside a native Text component.', 'Keep the import and View wrapper; edit the word inside Text.', 'import {View, Text} from "react-native";\nexport default function App() {\n  return <View><Text>Welcome</Text></View>;\n}', 'The native app displays Welcome.')
guide('nodejs', ['Runtime: software that executes a language.', 'Terminal: an interface for entering operating-system commands.', 'Argument: a value supplied to a program or function.', 'Module: a file with explicitly shared code.'],
 'Complete JavaScript first. On a computer with Node.js installed, save hello.mjs. Open a terminal in its folder and run node hello.mjs. A browser and internet connection are not required.',
 'const city = "Kabul";\nconsole.log(city);',
 ['Node executes the file outside the browser.', 'The first line binds Kabul to city.', 'console.log writes the value to the terminal. No DOM or document object is provided by Node.'],
 'Where does this example show its output?', ['The terminal', 'A browser heading', 'A phone notification'], 0,
 'Write a local script that displays Salam.', 'Use console.log with a quoted string and run the saved .mjs file.', 'console.log("Salam");', 'Salam')
guide('expressjs', ['Route: a rule matching a request method and path.', 'Request: a client’s message to a server.', 'Response: the server’s reply.', 'Loopback: an address that refers to the same computer.'],
 'Complete NodeJs first. Use a provisioned project with Express installed and an ES-module entry file named app.mjs. Run node app.mjs, then open http://127.0.0.1:3000/ in a browser on the same computer. This local address does not require internet.',
 'import express from "express";\nconst app = express();\napp.get("/", (req, res) => res.send("Salam"));\napp.listen(3000, "127.0.0.1");',
 ['express() creates an application with a route table.', 'The GET route answers requests for / by sending Salam.', 'listen starts the local service. Stop it with Ctrl+C in its terminal after practicing. This example has no database or authentication.'],
 'What does a GET request to / receive?', ['Salam', 'The source file', 'Nothing'], 0,
 'Change the route response to Welcome.', 'Edit the string passed to res.send and restart the local service.', 'import express from "express";\nconst app = express();\napp.get("/", (req, res) => res.send("Welcome"));\napp.listen(3000, "127.0.0.1");', 'The local browser displays Welcome.')
guide('flutter-dart', ['Dart: the programming language used here.', 'Function: a named group of instructions.', 'Widget: a description of part of a Flutter interface.', 'print: a Dart function that writes a value to the console.'],
 'No programming experience is required. Start with Dart before widgets. On a computer with Flutter/Dart provisioned, save main.dart and run dart run main.dart. This first lesson uses the console, not a mobile screen.',
 'void main() {\n  final city = "Kabul";\n  print(city);\n}',
 ['main is where this program starts. void means it returns no value to its caller.', 'final creates a binding that is assigned once.', 'print displays Kabul in the console. In a Flutter interface, use a Text widget instead when the user should see text on screen.'],
 'Where does print(city) display Kabul?', ['The console', 'A Text widget automatically', 'A database'], 0,
 'Declare greeting with final and display Salam.', 'Keep the main function and change both the binding and print argument.', 'void main() {\n  final greeting = "Salam";\n  print(greeting);\n}', 'Salam')
