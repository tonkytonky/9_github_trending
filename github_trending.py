import argparse
from datetime import datetime, timedelta
import requests
from urllib.parse import urljoin


def _main():
    args = get_args(argparse.ArgumentParser())
    trending_repositories = get_trending_repositories(args.number, args.days)
    for trending_repository in trending_repositories:
        print('issues: {}, link: {}'.format(
            trending_repository['issues'],
            trending_repository['link'])
        )


def get_args(parser):
    parser.add_argument(
        '-n',
        '--number',
        help='Number of repositories to get',
        type=int,
        default=20
    )
    parser.add_argument(
        '-d',
        '--days',
        help='Number of days for which to get repositories',
        type=int,
        default=7
    )

    return parser.parse_args()


def get_trending_repositories(top_size, days):
    start_date = datetime.now() - timedelta(days=days)
    repos = requests.get(
        url='https://api.github.com/search/repositories',
        params={
            'q': 'created:>2018-02-15'.format(start_date.strftime('%Y-%m-%d')),
            'sort': 'stars',
            'order': 'desc',
        }
    ).json()

    for repo in repos['items'][:top_size]:
        open_issues_amount = get_open_issues_amount(
            repo['owner']['login'],
            repo['name']
        )
        link = repo['html_url']
        yield {'issues': open_issues_amount, 'link': link}


def get_open_issues_amount(repo_owner, repo_name):
    url = urljoin(
        'https://api.github.com',
        'repos/{repo_owner}/{repo_name}/issues'.format(
            repo_owner=repo_owner,
            repo_name=repo_name,
        )
    )
    return len(requests.get(url).json())


if __name__ == '__main__':
    _main()
