module.exports = class Feedback {
	constructor(recruit, repo, status) {
		this.recruit = recruit;
		this.repo = repo;
		this.status = status;
	}

	send_feedback() {
		switch (this.status.toLowerCase()) {
			case 'excellent':
				return this.excellent_message();
			case 'competent':
				return this.competent_message();
			case 'not competent':
				return this.not_competent_message();
			case 'red flag':
				return this.red_flag_message();

			default:
				return 'Invalid entry';
		}
	}

	competent_message() {
		let subject = `Hey @${this.recruit}`;
		let body = `I was reviewing your ${this.repo}. I have marked you  as competent. Well done and keep it up.\n\nThank you.`;

		return subject + '\n' + body;
	}

	excellent_message() {
		let subject = `Hey @${this.recruit}`;
		let body = `I was reviewing your ${this.repo}. I found your work to be **Excellent**. I really love your logic and 'outside the box' thinking. Please continue to do this and Keep it up. Could you also help your fellow peers and show them how you approached this project.`;
		let conclusion = '\n\nThank you.';

		return subject + '\n' + body + conclusion;
	}

	not_competent_message() {
		let subject = `Hey @${this.recruit}`;
		let body = `I was reviewing your ${this.repo}. I found some issues I would like for you to fix:`;
		let conclusion =
			'Please fix the issues mentioned above. If you have any questions, feel free to contact me.\n\nThank you.';

		return subject + '\n' + body + '\n' + conclusion;
	}

	red_flag_message() {
		let subject = `Hey @${this.recruit}`;
		let body = `I was reviewing your ${this.repo}. I have marked you as a **RED FLAG**. Here are some of the major issues:`;
		let conclusion =
			'Please fix the issues mentioned above. If you have any questions, feel free to contact me.\n\nThank you.';

		return subject + '\n' + body + '\n' + conclusion;
	}
};
