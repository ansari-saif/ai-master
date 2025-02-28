export type ValidationError = {
	loc: Array<string | number>;
	msg: string;
	type: string;
};



export type ModuleCreate = {
	title: string;
	description: string;
};



export type ModuleRead = {
	id: number;
	title: string;
	description: string;
};



export type ModuleUpdate = {
	title?: string;
	description?: string;
};

