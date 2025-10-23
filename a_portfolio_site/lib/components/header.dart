import 'package:jaspr/jaspr.dart';
import 'package:jaspr_router/jaspr_router.dart';

class Header extends StatelessComponent {
  @override
  Iterable<Component> build(BuildContext context) sync* {
    yield header(
      classes: 'bg-white shadow-sm py-4 px-6 md:px-10 flex justify-between items-center',
      children: [
        a(
          href: '/',
          classes: 'text-2xl font-bold text-indigo-600 hover:text-indigo-800',
          children: [text('YourName.')],
        ),
        nav(
          classes: 'space-x-4',
          children: [
            Router.link(
              path: '/',
              classes: 'text-gray-600 hover:text-indigo-600 text-lg font-medium transition-colors duration-200',
              children: [text('Home')],
            ),
            Router.link(
              path: '/projects',
              classes: 'text-gray-600 hover:text-indigo-600 text-lg font-medium transition-colors duration-200',
              children: [text('Projects')],
            ),
            // Add more links here like 'About' or 'Contact'
          ],
        ),
      ],
    );
  }
}
