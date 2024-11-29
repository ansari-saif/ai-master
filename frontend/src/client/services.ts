import type { CancelablePromise } from './core/CancelablePromise';
import { OpenAPI } from './core/OpenAPI';
import { request as __request } from './core/request';

import type { Patient_managementCreate,Patient_managementRead,Doctor_managementCreate,Doctor_managementRead,Asset_managementCreate,Asset_managementRead } from './models';

export type PatientManagementData = {
        CreatePatientManagementApiV1PatientManagementPost: {
                    requestBody: Patient_managementCreate
                    
                };
    }

export type DoctorManagementData = {
        CreateDoctorManagementApiV1DoctorManagementPost: {
                    requestBody: Doctor_managementCreate
                    
                };
    }

export type AssetManagementData = {
        CreateAssetManagementApiV1AssetManagementPost: {
                    requestBody: Asset_managementCreate
                    
                };
    }

export class PatientManagementService {

	/**
	 * List All Patient_management
	 * @returns Patient_managementRead Successful Response
	 * @throws ApiError
	 */
	public static listAllPatientManagementApiV1PatientManagementGet(): CancelablePromise<Array<Patient_managementRead>> {
				return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/patient_management/',
		});
	}

	/**
	 * Create Patient_management
	 * @returns Patient_managementRead Successful Response
	 * @throws ApiError
	 */
	public static createPatientManagementApiV1PatientManagementPost(data: PatientManagementData['CreatePatientManagementApiV1PatientManagementPost']): CancelablePromise<Patient_managementRead> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/patient_management/',
			body: requestBody,
			mediaType: 'application/json',
		});
	}

}

export class DoctorManagementService {

	/**
	 * List All Doctor_management
	 * @returns Doctor_managementRead Successful Response
	 * @throws ApiError
	 */
	public static listAllDoctorManagementApiV1DoctorManagementGet(): CancelablePromise<Array<Doctor_managementRead>> {
				return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/doctor_management/',
		});
	}

	/**
	 * Create Doctor_management
	 * @returns Doctor_managementRead Successful Response
	 * @throws ApiError
	 */
	public static createDoctorManagementApiV1DoctorManagementPost(data: DoctorManagementData['CreateDoctorManagementApiV1DoctorManagementPost']): CancelablePromise<Doctor_managementRead> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/doctor_management/',
			body: requestBody,
			mediaType: 'application/json',
		});
	}

}

export class AssetManagementService {

	/**
	 * List All Asset_management
	 * @returns Asset_managementRead Successful Response
	 * @throws ApiError
	 */
	public static listAllAssetManagementApiV1AssetManagementGet(): CancelablePromise<Array<Asset_managementRead>> {
				return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/asset_management/',
		});
	}

	/**
	 * Create Asset_management
	 * @returns Asset_managementRead Successful Response
	 * @throws ApiError
	 */
	public static createAssetManagementApiV1AssetManagementPost(data: AssetManagementData['CreateAssetManagementApiV1AssetManagementPost']): CancelablePromise<Asset_managementRead> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/asset_management/',
			body: requestBody,
			mediaType: 'application/json',
		});
	}

}