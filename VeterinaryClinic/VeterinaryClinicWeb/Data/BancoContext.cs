using Microsoft.EntityFrameworkCore;
using VeterinaryClinicWeb.Models;
using VeterinaryClinic.BL;
using VeterinaryClinicWeb.Mappings;

namespace VeterinaryClinicWeb.Data
{
    public class BancoContext : DbContext
    {
        public BancoContext(DbContextOptions<BancoContext>? options) : base(options)
        {
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.ApplyConfiguration(new AnimalMap());
            modelBuilder.ApplyConfiguration(new AnimalResponsibleMap());
            modelBuilder.ApplyConfiguration(new AttendanceMap());
            modelBuilder.ApplyConfiguration(new ClinicMap());
            modelBuilder.ApplyConfiguration(new PersonMap());
            modelBuilder.ApplyConfiguration(new ProcedureMap());
            modelBuilder.ApplyConfiguration(new RaceMap());
            modelBuilder.ApplyConfiguration(new SpecieMap());
            modelBuilder.ApplyConfiguration(new VetMap());
        }

        public DbSet<Clinic> Clinics { get; set; }

        public DbSet<Procedure> Procedures { get; set; }

        public DbSet<Specie> Species { get; set; }

        public DbSet<Race> Races { get; set; }

        public DbSet<Person> Persons { get; set; }

        public DbSet<AnimalResponsible> AnimalResponsibles { get; set; }

        public DbSet<Vet> Vets { get; set; }

        public DbSet<Animal> Animals { get; set; }

        public DbSet<Attendance> Attendances { get; set; }
    }
}
