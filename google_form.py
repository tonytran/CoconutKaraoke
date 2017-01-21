"""
Submit data to a Google Form
"""
import logging
import warnings


class LyricResponseForm(object):
    """
    Form to allow users to submit lyrics to the Google Form.
    """

    def __init__(self):
        """
        Configuration for the form.
        """
        self.form_id = '1FAIpQLSc6_zSrL8-2-k7K3l2Z7PugmuHh7lzhd_63gxT6Q4WTvG_6yA'

        self.response_url = 'https://docs.google.com/forms/d/e/{}/formResponse'.format(self.form_id)

        self.genres = [
            'Rap',
            'Hiphop',
            'Country',
            'Rock'
        ]

        self.user_agent = {
            'Referer': 'https://docs.google.com/forms/d/e/{}/viewform'.format(self.form_id),
            'User-Agent': (
                'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36'
            )
        }

    def save(self, genre, *args):
        """
        Save the data entered into the form.
        A genre (str) followed by eight lyrics (str) are expected.
        """
        import requests

        # Validate that a known genre was entered
        if genre not in self.genres:
            # Just warn about the issue, don't make anything fail
            warnings.warn(
                '{} is not a known genre'.format(genre)
            )

        # Check that the form was completely filled out
        if len(args) != 8:
            warnings.warn(
                '{} args provided, expected 8'.format(len(args))
            )

        form_data = {
            'entry.899231417': genre,
            'entry.1872476949': args[0],
            'entry.1384112731': args[1],
            'entry.335553084': args[2],
            'entry.1927967575': args[3],
            'entry.1856417683': args[4],
            'entry.1774565447': args[5],
            'entry.284759774': args[6],
            'entry.243965201': args[7],
            'draftResponse': [],
            'pageHistory': 0
        }

        response = requests.post(self.response_url, data=form_data, headers=self.user_agent)

        logging.info(response.text)


form = LyricResponseForm()

form.save(
    'Country',
    'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H'
)