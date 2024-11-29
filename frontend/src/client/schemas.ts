export const $Patient_managementCreate = {
	properties: {
		name: {
	type: 'string',
	isRequired: true,
},
		age: {
	type: 'number',
	isRequired: true,
},
		gender: {
	type: 'string',
	isRequired: true,
},
		contact_information: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $Patient_managementRead = {
	properties: {
		id: {
	type: 'number',
	isRequired: true,
},
		name: {
	type: 'string',
	isRequired: true,
},
		age: {
	type: 'number',
	isRequired: true,
},
		gender: {
	type: 'string',
	isRequired: true,
},
		contact_information: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $Doctor_managementCreate = {
	properties: {
		name: {
	type: 'string',
	isRequired: true,
},
		specialty: {
	type: 'string',
	isRequired: true,
},
		contact_information: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $Doctor_managementRead = {
	properties: {
		id: {
	type: 'number',
	isRequired: true,
},
		name: {
	type: 'string',
	isRequired: true,
},
		specialty: {
	type: 'string',
	isRequired: true,
},
		contact_information: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $Asset_managementCreate = {
	properties: {
		asset_name: {
	type: 'string',
	isRequired: true,
},
		quantity: {
	type: 'number',
	isRequired: true,
},
		location: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $Asset_managementRead = {
	properties: {
		id: {
	type: 'number',
	isRequired: true,
},
		asset_name: {
	type: 'string',
	isRequired: true,
},
		quantity: {
	type: 'number',
	isRequired: true,
},
		location: {
	type: 'string',
	isRequired: true,
},
	},
} as const;