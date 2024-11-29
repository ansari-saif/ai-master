export type TodoCreate = {
	title: string;
	description?: string | null;
	is_completed?: boolean;
};



export type TodoRead = {
	id: number;
	title: string;
	description?: string | null;
	is_completed: boolean;
};



export type TodoUpdateSchema = {
	title?: string | null;
	description?: string | null;
	is_completed?: boolean | null;
};



export type ValidationError = {
	loc: Array<string | number>;
	msg: string;
	type: string;
};



export type Patient_managementCreate = {
	name: string;
	age: number;
	gender: string;
	contact_information: string;
};



export type Patient_managementRead = {
	id: number;
	name: string;
	age: number;
	gender: string;
	contact_information: string;
};



export type Doctor_managementCreate = {
	name: string;
	specialty: string;
	contact_information: string;
};



export type Doctor_managementRead = {
	id: number;
	name: string;
	specialty: string;
	contact_information: string;
};



export type Asset_managementCreate = {
	asset_name: string;
	quantity: number;
	location: string;
};



export type Asset_managementRead = {
	id: number;
	asset_name: string;
	quantity: number;
	location: string;
};

