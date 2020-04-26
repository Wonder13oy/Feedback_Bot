Feedback_Bot = require('../src/app/Feedback_Class');

let feedback = new Feedback_Bot(
	'wandile',
	'Wonder13oy/example',
	'Not competent',
);

describe('Constructor', () => {
	it('should declare and define the recruit', () => {
		expect(feedback.recruit).toBe('wandile');
	});

	it('should declare and define the status', () => {
		expect(feedback.status).toBe('Not competent');
	});

	it('should declare and define the repo', () => {
		expect(feedback.repo).toBe('Wonder13oy/example');
	});
});

describe('not_competent_message()', () => {
	it('should return the correct message for non-competent recruits', () => {
		let message = feedback.not_competent_message();

		expect(message).toBe(
			'Hey @wandile\nI was reviewing your Wonder13oy/example. I found some issues I would like for you to fix:\nPlease fix the issues mentioned above. If you have any questions, feel free to contact me.\n\nThank you.',
		);
	});
});

describe('send_feedback()', () => {
	it('should return the correct message for non-competent recruits', () => {
		let message = feedback.send_feedback();

		expect(message).toBe(
			'Hey @wandile\nI was reviewing your Wonder13oy/example. I found some issues I would like for you to fix:\nPlease fix the issues mentioned above. If you have any questions, feel free to contact me.\n\nThank you.',
		);

		let feedback2 = new Feedback_Bot(
			'wandile',
			'Wonder13oy/example',
			'cOmpetEnt',
		);
		message = feedback2.send_feedback();

		expect(message).toBe(
			'Hey @wandile\nI was reviewing your Wonder13oy/example. I have marked you  as competent. Well done and keep it up.\n\nThank you.',
		);
	});
});
