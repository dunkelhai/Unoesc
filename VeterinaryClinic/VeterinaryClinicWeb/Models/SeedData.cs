using Microsoft.EntityFrameworkCore;
using VeterinaryClinicWeb.Data;
using VeterinaryClinic.BL;

namespace VeterinaryClinicWeb.Models
{
    public static class SeedData
    {

        public static void EnsurePopulated(IApplicationBuilder app)
        {
            BancoContext bancoContext = app.ApplicationServices.
                CreateScope().ServiceProvider.GetRequiredService<BancoContext>();

            if (bancoContext.Database.GetPendingMigrations().Any())
            {
                bancoContext.Database.Migrate();
            }

            if (!bancoContext.Clinics.Any())
            {
                bancoContext.Clinics.AddRange(new Clinic
                {
                    Name = "Vida Vet"
                }
                );
            }

            bancoContext.SaveChanges();

        }

    }
}
