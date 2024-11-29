export const $Patient_managementCreate = {
	properties: {
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
		contact_information: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $Doctor_managementCreate = {
	properties: {
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
		contact_information: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $Asset_managementCreate = {
	properties: {
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
		location: {
	type: 'string',
	isRequired: true,
},
	},
} as const;