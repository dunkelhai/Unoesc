using Microsoft.AspNetCore.Localization;
using Microsoft.EntityFrameworkCore;
using System.Globalization;
using VeterinaryClinicWeb.Data;
using VeterinaryClinicWeb.Models;
using VeterinaryClinicWeb.Models.EF.Interfaces;
using VeterinaryClinicWeb.Models.EF.Repositories;

var builder = WebApplication.CreateBuilder(args);


// Add services to the container.
builder.Services.AddControllersWithViews();

builder.Services.AddDbContext<BancoContext>
    (options => options.UseSqlServer("Server=localhost;Database=VeterinaryClinic;User ID=SA;Password=12345OHdf%e;MultipleActiveResultSets=True;"));


builder.Services.AddScoped<IClinicRepository, ClinicRepository>();
builder.Services.AddScoped<IProcedureRepository, ProcedureRepository>();
builder.Services.AddScoped<ISpecieRepository, SpecieRepository>();
builder.Services.AddScoped<IRaceRepository, RaceRepository>();
builder.Services.AddScoped<IAnimalResponsibleRepository, AnimalResponsibleRepository>();
builder.Services.AddScoped<IVetRepository, VetRepository>();
builder.Services.AddScoped<IAnimalRepository, AnimalRepository>();
builder.Services.AddScoped<IAttendanceRepository, AttendanceRepository>();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseStatusCodePages();
app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapDefaultControllerRoute();

/*app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");
*/

SeedData.EnsurePopulated(app);

app.Run();