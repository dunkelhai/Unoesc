using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using VeterinaryClinic.BL;

namespace VeterinaryClinicWeb.Mappings
{
    public class PersonMap : IEntityTypeConfiguration<Person>
    {
        public void Configure(EntityTypeBuilder<Person> builder)
        {
            builder.ToTable("Person");

            builder.Property(p => p.Name)
                .HasColumnType("varchar(100)")
                .IsRequired();

            builder.Property(p => p.Email)
                .HasColumnType("varchar(100)")
                .IsRequired();

            builder.Property(p => p.CPF)
                .HasColumnType("varchar(11)")
                .IsRequired();

            builder.Property(p => p.Phone)
                .HasColumnType("varchar (15)");

            builder.Property(p => p.Gender)
                .HasColumnType("varchar(8)")
                .IsRequired();
        }
    }
}