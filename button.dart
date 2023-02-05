import 'package:flutter/material.dart';

void main() {
  runApp(const Button());
}

//
class Button extends StatefulWidget {
  const Button({super.key});

  @override
  State<Button> createState() => _MainAppState();
}

class _MainAppState extends State<Button> {
  int count = 0;
  void incrementCounter() {
    setState(() {
      count++;
    });
  }

  Widget outlinedButton() {
    return OutlinedButton(
      onPressed: incrementCounter,
      child: Padding(
        padding: const EdgeInsets.all(18.0),
        child: Text(
          "Clicks - $count",
          style: TextStyle(
            fontSize: 20,
            color: Color.fromARGB(255, 0, 138, 53),
          ),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Center(
          child: outlinedButton(),
        ),
      ),
    );
  }
}
