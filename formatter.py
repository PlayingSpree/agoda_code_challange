def formatRequest(res,info,repository):
    if info == 'pull-requests':
        print('Repository {} top 10 pull requests are: '.format(repository))
        print()
        for pull in res:
            print('PR-{} - {}'.format(str(pull['number']),pull['title']))
            print('Created by {} on {}'.format(pull['user']['login'],pull['created_at']))
            print('PR is {}'.format(pull['state']))
            print()
    elif info == 'issues':
        print('Repository {} top 10 pull issues are: '.format(repository))
        for issue in res:
            print('#{} - {}'.format(str(issue['number']),issue['title']))
            print('Created by {} on {}'.format(issue['user']['login'],issue['created_at']))
            print('Issue is {}'.format(issue['state']))
            print()
    