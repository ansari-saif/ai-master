export type ValidationError = {
	loc: Array<string | number>;
	msg: string;
	type: string;
};



export type ModuleCreate = {
	title: string;
};



export type ModuleRead = {
	id: number;
	title: string;
};



export type ModuleUpdate = {
	title?: string;
};

