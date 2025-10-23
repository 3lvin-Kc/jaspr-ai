import 'package:jaspr/jaspr.dart';

class Footer extends StatelessComponent {
  @override
  Iterable<Component> build(BuildContext context) sync* {
    yield footer(
      classes: 'bg-gray-800 text-white py-6 text-center text-sm',
      children: [
        p(
          children: [text('© ${DateTime.now().year} Your Name. All rights reserved.')],
        ),
        p(
          classes: 'mt-2',
          children: [
            a(
              href: '#',
              classes: 'text-gray-400 hover:text-white mx-2',
              children: [text('LinkedIn')],
            ),
            a(
              href: '#',
              classes: 'text-gray-400 hover:text-white mx-2',
              children: [text('GitHub')],
            ),
          ],
        ),
      ],
    );
  }
}
