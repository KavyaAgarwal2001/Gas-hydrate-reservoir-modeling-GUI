#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#define X 10
#define T 60
#define f 10.0
#define t0 0.0
#define rp 1
#define sp 1
double real_data[T];
double real_data_step[T];
double residual[T];
double cr[X];
double mr[X];
double gradu[X];
double ur_past[X], ur_futr[X], ur_prsnt[X];
double gather_real[T];
double ms[X];
double cs[X];
double grad[X];
double uas_past[X], uas_futr[X], uas_prsnt[X];
double uns_past[X], uns_futr[X], uns_prsnt[X];
double gather_mkpedk[T];
double mkpedk_past[X], mkpedk_futr[X], mkpedk_prsnt[X];
double dx;
double dt;
//double dx;
//	double dt;
//	int rp;
//	int T;
//	double f;
//	int X;
double largest(double vec[])
{
	int i;
	double max = vec[0];
	for (i = 0; i < X; i++)
		if (vec[i] > max)
			max = vec[i];
	return max;
}
int main()
{
//	double dx;
//	FILE *para;
//	para = fopen("parameter.txt", "r");
//	fscanf(para, "%lf", &dx); //spatial
//	fscanf(para, "%lf\n", &dt); //temporal
//	fscanf(para, "%d\n", &rp);	//receiver
//	fscanf(para, "%d\n", &T);	//recording time
//	fscanf(para, "%lf\n", &f);	//freq
//	fscanf(para, "%d\n", &X);	//Depth
	double objective;
	FILE *fobj;
	fobj = fopen("fobj.txt", "w");

	int i, j;
	int t;
	int maxitr = 10;
	double dx = 5.0;
	double dt = 0.001;
	double ti;
	double source_real;
	FILE *read_synthetic_model;
	read_synthetic_model = fopen("synthetic_model.txt", "r");
	for (i = 0; i < X; i++)
	{
		fscanf(read_synthetic_model, "%lf", &cs[i]);
	}
	// synthetic data

	double source_synt;
	double second_der_ns[i];
	for (int itr = 0; itr < maxitr; itr++)
	{

		cs[0] = 2000.0;
		cs[X - 1] = 2000.0;
		double gather_synt[T];
		double us_past[X], us_futr[X], us_prsnt[X];
		for (i = 0; i < X; i++)
		{
			us_past[i] = 0.0;
			us_futr[i] = 0.0;
			us_prsnt[i] = 0.0;
		}
		for (t = 0; t < T; t++)
		{
			ti = t * dt;
			source_synt = (1 - (2 * 3.14 * 3.14 * f * f * ((ti - t0) * (ti - t0)))) * exp(-1 * 3.14 * 3.14 * f * f * ((ti - t0) * (ti - t0)));
			us_prsnt[sp] = us_prsnt[sp] + source_synt / dx * dt * dt;
			for (i = 1; i < X - 1; i++)
			{
				us_futr[i] = ((((cs[i] * cs[i])) * dt * dt) / (dx * dx)) * (us_prsnt[i + 1] - 2 * us_prsnt[i] + us_prsnt[i - 1]) + 2 * us_prsnt[i] - us_past[i];
			}
			for (i = 0; i < X; i++)
			{
				us_past[i] = us_prsnt[i];
				us_prsnt[i] = us_futr[i];
			}
			gather_synt[t] = us_prsnt[rp];
		}
		// residual
		FILE *read_real;
		read_real = fopen("realamp1.txt", "r");
		FILE *residual_source;
		residual_source = fopen("residual_field.dat", "w");
		objective = 0.0;
		double obj;
		for (t = 0; t < T; t++)
		{
			fscanf(read_real, "%lf", &real_data[t]);
			residual[t] = -real_data[t] + gather_synt[t];
			fprintf(residual_source, "%0.50lf\n", residual[t]);
			objective = objective + residual[t] * residual[t];
		}
		if (itr == 0)
			obj = objective;
		fclose(residual_source);
		fprintf(fobj, "%0.50lf\n", objective / obj);
		// adjoint
		double source_as;
		double source_ns;
		for (i = 0; i < X; i++)
		{
			uas_past[i] = 0.0;
			uas_futr[i] = 0.0;
			uas_prsnt[i] = 0.0;
		}
		for (i = 0; i < X; i++)
		{
			uns_past[i] = 0.0;
			uns_futr[i] = 0.0;
			uns_prsnt[i] = 0.0;
		}
		for (i = 0; i < X; i++)
		{
			gradu[i] = 0.0;
		}
		for (t = 0; t < T; t++)
		{
			ti = t * dt;
			source_as = residual[T - 1 - t];
			//	source_as = residual[t];
			//	printf("adjoint source is %0.50lf\n", source_as);
			source_ns = (1 - (2 * 3.14 * 3.14 * f * f * ((ti - t0) * (ti - t0)))) * exp(-1 * 3.14 * 3.14 * f * f * ((ti - t0) * (ti - t0)));
			uas_prsnt[sp] = uas_prsnt[sp] + source_as / dx * dt * dt;
			uns_prsnt[sp] = uns_prsnt[sp] + source_ns / dx * dt * dt;
			for (i = 1; i < X - 1; i++)
			{
				second_der_ns[i] = (2 / (cs[i] * cs[i] * cs[i])) * ((uns_futr[i] - 2 * uns_prsnt[i] + uns_past[i]) / (dt * dt));

				if (i == 8)
					gradu[i] = (gradu[i] - (uas_prsnt[i] * second_der_ns[i]));
				uas_futr[i] = (((cs[i] * cs[i]) * dt * dt) / (dx * dx)) * (uas_prsnt[i + 1] - 2 * uas_prsnt[i] + uas_prsnt[i - 1]) + 2 * uas_prsnt[i] - uas_past[i];
				uns_futr[i] = (((cs[i] * cs[i]) * dt * dt) / (dx * dx)) * (uns_prsnt[i + 1] - 2 * uns_prsnt[i] + uns_prsnt[i - 1]) + 2 * uns_prsnt[i] - uns_past[i];
			}
			for (i = 0; i < X; i++)
			{
				uas_past[i] = uas_prsnt[i];
				uas_prsnt[i] = uas_futr[i];
				uns_past[i] = uns_prsnt[i];
				uns_prsnt[i] = uns_futr[i];
			}
			double adj_field_gather[T];
			double normal_field_gather[T];
			adj_field_gather[t] = uas_prsnt[rp];
			normal_field_gather[t] = uns_prsnt[rp];
		}

		// step length
		double grad_mod[T];
		for (i = 0; i < X; i++)
		{
			if (gradu[i] < 0)
				grad_mod[i] = -1 * gradu[i];
			else
				grad_mod[i] = gradu[i];
		}
		double maximum_grad;
		maximum_grad = largest((grad_mod));
		double maximum_model;
		maximum_model = largest(cs);
		double epsilon;
		epsilon = maximum_model / (100.0 * maximum_grad);
		double mk_plus_edk[X];
		for (i = 0; i < X; i++)
		{
			mk_plus_edk[i] = cs[i] + epsilon * gradu[i];
		}
		for (i = 0; i < X; i++)
		{
			mkpedk_past[i] = 0.0;
			mkpedk_futr[i] = 0.0;
			mkpedk_prsnt[i] = 0.0;
		}
		for (t = 0; t < T; t++)
		{
			ti = t * dt;
			source_synt = (1 - (2 * 3.14 * 3.14 * f * f * ((ti - t0) * (ti - t0)))) * exp(-1 * 3.14 * 3.14 * f * f * ((ti - t0) * (ti - t0)));
			mkpedk_prsnt[sp] = mkpedk_prsnt[sp] + source_synt / dx * dt * dt;
			for (i = 1; i < X - 1; i++)
			{
				mkpedk_futr[i] = (((mk_plus_edk[i] * mk_plus_edk[i]) * dt * dt) / (dx * dx)) * (mkpedk_prsnt[i + 1] - 2 * mkpedk_prsnt[i] + mkpedk_prsnt[i - 1]) + 2 * mkpedk_prsnt[i] - mkpedk_past[i];
			}
			for (i = 0; i < X; i++)
			{
				mkpedk_past[i] = mkpedk_prsnt[i];
				mkpedk_prsnt[i] = mkpedk_futr[i];
			}
			gather_mkpedk[t] = mkpedk_prsnt[rp];
		}
		double jkdk[T];
		for (t = 0; t < T; t++)
		{
			jkdk[t] = (gather_mkpedk[t] - gather_synt[t]) / epsilon;
		}
		double alpha1;
		double alpha2;
		alpha1 = 0;
		alpha2 = 0;
		for (t = 0; t < T; t++)
		{
			alpha1 = alpha1 + jkdk[t] * (real_data[t] - gather_synt[t]);
			alpha2 = alpha2 + jkdk[t] * jkdk[t];
		}
		double alpha;
		alpha = alpha1 / alpha2;
		//update
		for (i = 1; i < X - 1; i = i + 1)
		{
			cs[i] = cs[i] + alpha * gradu[i];
		}
		fclose(read_real);
	}
	FILE *result;
	result = fopen("result_model.txt", "w");
	for (i = 0; i < X; i++)
	{
		fprintf(result, "%lf\n", cs[i]);
		printf("velocity at %d grid is %lf\n", i, cs[i]);
	}
	return 0;
}
