export const $ValidationError = {
	properties: {
		loc: {
	type: 'array',
	contains: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'number',
}],
},
	isRequired: true,
},
		msg: {
	type: 'string',
	isRequired: true,
},
		type: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $ModuleCreate = {
	properties: {
		title: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $ModuleRead = {
	properties: {
		id: {
	type: 'number',
	isRequired: true,
},
		title: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $ModuleUpdate = {
	properties: {
		title: {
	type: 'string',
},
	},
} as const;