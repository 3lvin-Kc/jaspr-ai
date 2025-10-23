import 'package:jaspr/jaspr.dart';

class ProjectsPage extends StatelessComponent {
  @override
  Iterable<Component> build(BuildContext context) sync* {
    yield div(
      classes: 'container mx-auto px-6 py-12 md:py-16',
      children: [
        h1(
          classes: 'text-4xl font-extrabold text-gray-900 text-center mb-10',
          children: [text('My Projects')],
        ),
        div(
          classes: 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8',
          children: [
            _buildProjectCard(
              'Project Alpha',
              'A cutting-edge web application for data visualization.',
              'https://via.placeholder.com/300x200?text=Project+Alpha',
            ),
            _buildProjectCard(
              'Project Beta',
              'An innovative mobile-first e-commerce solution.',
              'https://via.placeholder.com/300x200?text=Project+Beta',
            ),
            _buildProjectCard(
              'Project Gamma',
              'A community platform built with real-time features.',
              'https://via.placeholder.com/300x200?text=Project+Gamma',
            ),
            _buildProjectCard(
              'Project Delta',
              'A personal blog and content management system.',
              'https://via.placeholder.com/300x200?text=Project+Delta',
            ),
            // Add more project cards here
          ],
        ),
      ],
    );
  }

  Component _buildProjectCard(String title, String description, String imageUrl) {
    return div(
      classes: 'bg-white rounded-lg shadow-md hover:shadow-xl transition-shadow duration-300 overflow-hidden',
      children: [
        img(
          src: imageUrl,
          alt: title,
          classes: 'w-full h-48 object-cover',
        ),
        div(
          classes: 'p-6',
          children: [
            h2(
              classes: 'text-2xl font-bold text-gray-900 mb-2',
              children: [text(title)],
            ),
            p(
              classes: 'text-gray-700 leading-relaxed mb-4',
              children: [text(description)],
            ),
            a(
              href: '#',
              classes: 'text-indigo-600 hover:text-indigo-800 font-medium',
              children: [text('Learn More')],
            ),
          ],
        ),
      ],
    );
  }
}
