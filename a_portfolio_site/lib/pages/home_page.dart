import 'package:jaspr/jaspr.dart';
import 'package:jaspr_router/jaspr_router.dart';

class HomePage extends StatelessComponent {
  @override
  Iterable<Component> build(BuildContext context) sync* {
    yield div(
      classes: 'container mx-auto px-6 py-12 md:py-24 text-center',
      children: [
        img(
          src: 'https://via.placeholder.com/150',
          alt: 'Profile Picture',
          classes: 'rounded-full w-40 h-40 object-cover mx-auto mb-6 shadow-lg',
        ),
        h1(
          classes: 'text-5xl font-extrabold text-gray-900 mb-4',
          children: [text('Hello, I\'m Your Name.')],
        ),
        p(
          classes: 'text-xl text-gray-600 max-w-2xl mx-auto mb-8',
          children: [text('A passionate software developer building modern web applications with Jaspr and Dart. I love crafting elegant solutions to complex problems.')],
        ),
        Router.link(
          path: '/projects',
          classes: 'inline-block bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-3 px-8 rounded-lg shadow-lg transition-colors duration-300',
          children: [text('View My Work')],
        ),
      ],
    );
  }
}
