import 'package:jaspr/jaspr.dart';
import 'package:jaspr_router/jaspr_router.dart';
import 'components/footer.dart';
import 'components/header.dart';
import 'pages/home_page.dart';
import 'pages/projects_page.dart';

class App extends StatelessComponent {
  @override
  Iterable<Component> build(BuildContext context) sync* {
    yield Router(
      routes: [
        Route(
          path: '/',
          builder: (context, state) => HomePage(),
        ),
        Route(
          path: '/projects',
          builder: (context, state) => ProjectsPage(),
        ),
      ],
      builder: (context, child) sync* {
        yield div(
          classes: 'min-h-screen flex flex-col',
          children: [
            Header(),
            div(
              classes: 'flex-grow',
              children: [child],
            ),
            Footer(),
          ],
        );
      },
    );
  }
}
