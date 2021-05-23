#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#define X 10
#define T 100
#define f 10.0
#define t0 0.0
#define rp 1
#define sp 1
double real_data[T];
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
//int i, j, t;
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
    FILE *para;
    para = fopen("parameter.txt", "r");
    int *maxitr;
    maxitr = (int*)malloc(1*sizeof(int));
    maxitr[0] = 2;
    double *dx;
    dx = (double*)malloc(1*sizeof(double));
    dx[0] =5.0;

 //   fscanf(para, "%lf", &cr[i]);
	double objective;
	FILE *fobj;
	fobj = fopen("fobj.dat", "w");
	FILE *fnorm_grad;
	fnorm_grad = fopen("norm_grad.dat", "w");
	FILE *field;
	field = fopen("field2.dat", "w");
	int i, j;
	int t;
	//int maxitr = 2;
	//	double residual[T];
	//double dx[0] = 5.0,
     double dt = 0.001;
	double ti;
	// real data
	double source_real;
	//	double cr[X];
	//	double mr[X];
	//	double gradu[X];
	for (i = 0; i < X; i++)
	{
		cs[i] = 2000.0;
		cs[8] = 2000.0;
		if (i >= 50 && i <= 60)
			cs[i] = 2050.0;
		if (i >= 40 && i < 50)
			cs[i] = 2050.0;
		//	ms[i] = 1 / (cs[i] * cs[i]);
	}
	for (i = 0; i < X; i++)
	{
		cr[i] = 2000.0;
		cr[8] = 2100.0;
		if (i >= 40 && i <= 60)
			cr[i] = 2000.0;
		if (i >= 40 && i < 50)
			cr[i] = 2000.0;
		//	printf("%lf\n", cr[i]);
		//	mr[i] = 1 / (cr[i] * cr[i]);
	}
	//	double ur_past[X], ur_futr[X], ur_prsnt[X];
	//	double gather_real[T];
	for (i = 0; i < X; i++)
	{
		ur_past[i] = 0.0;
		ur_futr[i] = 0.0;
		ur_prsnt[i] = 0.0;
	}
	for (t = 0; t < T; t++)
	{
		ti = t * dt;
		source_real = (1 - (2 * 3.14 * 3.14 * f * f * ((ti - t0) * (ti - t0)))) * exp(-1 * 3.14 * 3.14 * f * f * ((ti - t0) * (ti - t0)));
		ur_prsnt[sp] = ur_prsnt[sp] + source_real / dx[0] * dt * dt;
		for (i = 1; i < X - 1; i++)
		{
			ur_futr[i] = ((((cr[i] * cr[i])) * dt * dt) / (dx[0] * dx[0])) * (ur_prsnt[i + 1] - 2 * ur_prsnt[i] + ur_prsnt[i - 1]) + 2 * ur_prsnt[i] - ur_past[i];
		}
		for (i = 0; i < X; i++)
		{
			ur_past[i] = ur_prsnt[i];
			ur_prsnt[i] = ur_futr[i];
		}
		gather_real[t] = ur_prsnt[rp];
		fprintf(field, "%0.50lf\n", gather_real[t]);
	}
	fclose(field);
	// synthetic data
	double source_synt;
	//	double ms[X];
	//	double cs[X];
	/*	for (i = 0; i < X; i++)
	{
		cs[i] = 1500.0;		
	//	ms[i] = 1 / (cs[i] * cs[i]);
	}*/
	double second_der_ns[i];
	for (int itr = 0; itr < maxitr[0]; itr++)
	{
		FILE *adj_field;
		adj_field = fopen("adj_field.dat", "w");
		FILE *normal_field;
		normal_field = fopen("normal_field.dat", "w");
		cs[0] = 2000.0;
		cs[X - 1] = 2000.0;
		//	ms[0] = 1 / (cs[0] * cs[0]);
		//	ms[X - 1] = 1 / (cs[X - 1] * cs[X - 1]);
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
			us_prsnt[sp] = us_prsnt[sp] + source_synt / dx[0] * dt * dt;
			for (i = 1; i < X - 1; i++)
			{
				us_futr[i] = ((((cs[i] * cs[i])) * dt * dt) / (dx[0] * dx[0])) * (us_prsnt[i + 1] - 2 * us_prsnt[i] + us_prsnt[i - 1]) + 2 * us_prsnt[i] - us_past[i];
			}
			for (i = 0; i < X; i++)
			{
				us_past[i] = us_prsnt[i];
				us_prsnt[i] = us_futr[i];
			}
			gather_synt[t] = us_prsnt[rp];
		}
		// print residual
		FILE *read_real;
		read_real = fopen("field.dat", "r");
		FILE *residual_source;
		residual_source = fopen("residual_field.dat", "w");
		objective = 0.0;
		for (t = 0; t < T; t++)
		{
			fscanf(read_real, "%0.50lf", &real_data[t]);
			//	printf("%f\n",real_data[t]);
			//	residual[t] = -real_data[t] + gather_synt[t];
			residual[t] = -gather_real[t] + gather_synt[t];
			fprintf(residual_source, "%0.50lf\n", residual[t]);
			objective = objective + residual[t] * residual[t];
		}
		fclose(residual_source);
		fclose(read_real);
		fprintf(fobj, "%0.50lf\n", objective);
		// adjoint
		double source_as;
		double source_ns;
		//	double grad[X];
		//	double uas_past[X], uas_futr[X], uas_prsnt[X];
		//	double uns_past[X], uns_futr[X], uns_prsnt[X];
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
			uas_prsnt[sp] = uas_prsnt[sp] + source_as / dx[0] * dt * dt;
			uns_prsnt[sp] = uns_prsnt[sp] + source_ns / dx[0] * dt * dt;
			for (i = 1; i < X - 1; i++)
			{
				second_der_ns[i] = (2 / (cs[i] * cs[i] * cs[i])) * ((uns_futr[i] - 2 * uns_prsnt[i] + uns_past[i]) / (dt * dt));
				//	printf("%0.50lf\n", second_der_ns[i]);
			//	if (i >= 40 && i <= 60)
			if(i==8)
				gradu[i] = (gradu[i] - (uas_prsnt[i] * second_der_ns[i]));
				uas_futr[i] = (((cs[i] * cs[i]) * dt * dt) / (dx[0] * dx[0])) * (uas_prsnt[i + 1] - 2 * uas_prsnt[i] + uas_prsnt[i - 1]) + 2 * uas_prsnt[i] - uas_past[i];
				uns_futr[i] = (((cs[i] * cs[i]) * dt * dt) / (dx[0] * dx[0])) * (uns_prsnt[i + 1] - 2 * uns_prsnt[i] + uns_prsnt[i - 1]) + 2 * uns_prsnt[i] - uns_past[i];
				//	second_der_ns[i] = (2 / (cs[i] * cs[i] * cs[i])) * ((uns_futr[i] - 2 * uns_prsnt[i] + uns_past[i]) / (dt * dt));
				//	gradu[i] = (gradu[i] - (uas_prsnt[i] * second_der_ns[i]));
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
			fprintf(normal_field, "%0.50lf\n", normal_field_gather[t]);
			fprintf(adj_field, "%0.50lf\n", adj_field_gather[t]);
		}
		FILE *amp_ns;
		amp_ns = fopen("amplitude_n.txt", "w");
		FILE *amp_as;
		amp_as = fopen("amplitude_a.txt", "w");
		FILE *slope;
		slope = fopen("slope.txt", "w");
		for (i = 1; i < X - 1; i++)
		{
			fprintf(amp_as, "%0.80lf\n", uas_prsnt[i]);
			fprintf(amp_ns, "%0.80lf\n", second_der_ns[i]);
			fprintf(slope, "%0.80lf\n", gradu[i]);
		}
		fclose(amp_ns);
		fclose(amp_as);
		// norm of gradient
		double norm_grad = 0.0;
		for (i = 0; i < X; i++)
		{
			//	gradu[i] = gradu[i] * 2 * (pow(ms[i], 3));
			norm_grad = (norm_grad + gradu[i] * gradu[i]);
		}
		fprintf(fnorm_grad, "%0.50lf\n", norm_grad);
		// step length
		double grad_mod[T];
		for (i = 0; i < X; i++)
		{
			if (gradu[i] < 0)
				grad_mod[i] = -1 * gradu[i];
			else
				grad_mod[i] = gradu[i];
			//	printf("%0.50lf, %0.50lf\n",gradu[i], grad_mod[i]);
		}
		double maximum_grad;
		maximum_grad = largest((grad_mod));
		//	printf("%0.50lf\n", maximum_grad);
		double maximum_model;
		maximum_model = largest(cs);
		//	printf("%0.50lf\n", maximum_model);
		double epsilon;
		epsilon = maximum_model / (100.0 * maximum_grad);
		double mk_plus_edk[X];
		for (i = 0; i < X; i++)
		{
			mk_plus_edk[i] = cs[i] + epsilon * gradu[i];
		}
		//	double gather_mkpedk[T];
		//	double mkpedk_past[X], mkpedk_futr[X], mkpedk_prsnt[X];
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
			mkpedk_prsnt[sp] = mkpedk_prsnt[sp] + source_synt / dx[0] * dt * dt;
			for (i = 1; i < X - 1; i++)
			{
				mkpedk_futr[i] = (((mk_plus_edk[i] * mk_plus_edk[i]) * dt * dt) / (dx[0] * dx[0])) * (mkpedk_prsnt[i + 1] - 2 * mkpedk_prsnt[i] + mkpedk_prsnt[i - 1]) + 2 * mkpedk_prsnt[i] - mkpedk_past[i];
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
			alpha1 = alpha1 + jkdk[t] * (gather_real[t] - gather_synt[t]);
			alpha2 = alpha2 + jkdk[t] * jkdk[t];
		}
		double alpha;
		alpha = alpha1 / alpha2;
		//	printf("%lf\n", alpha);
		//update
		for (i = 1; i < X - 1; i = i + 1)
		{
			//if( i < 5)
			//	ms[i] = ms[i] + alpha * gradu[i];
			//		ms[i] = ms[i] - 0.0008*grad[i];
			cs[i] = cs[i] + alpha * gradu[i];
			//	cs[i] = 1 / sqrt(ms[i]);
		}
		for (i = 0; i < X; i++)
		{
			//	printf("gradient at position %d is %0.20f\n",i,grad[i]);
		}
	}
	for (i = 0; i < X; i++)
	{
		printf("velocity at %d grid is %lf\n", i, cs[i]);
	}
	return 0;
}
